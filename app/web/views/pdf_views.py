from flask import Blueprint, send_file, g, jsonify
import requests
from werkzeug.exceptions import Unauthorized
from app.web.hooks import login_required, handle_file_upload, load_model
from app.web.db.models import Pdf
from app.web.tasks.embeddings import process_document
from app.web import files
from app.web.config import Config
from io import BytesIO

bp = Blueprint("pdf", __name__, url_prefix="/api/pdfs")


@bp.route("/", methods=["GET"])
@login_required
def list():
    pdfs = Pdf.where(user_id=g.user.id)

    return Pdf.as_dicts(pdfs)


@bp.route("/", methods=["POST"])
@login_required
@handle_file_upload
def upload_file(file_id, file_path, file_name):
    res, status_code = files.upload(file_path)
    if status_code >= 400:
        return res, status_code

    pdf = Pdf.create(id=file_id, name=file_name, user_id=g.user.id)

    process_document.delay(pdf.id)

    return pdf.as_dict()


@bp.route("/<string:pdf_id>", methods=["GET"])
@login_required
@load_model(Pdf)
def show(pdf):
    return jsonify(
        {
            "pdf": pdf.as_dict(),
            "download_url": files.create_download_url(pdf.id),
        }
    )


@bp.route("/download/<string:file_id>", methods=["GET"])
@login_required
def proxy_download(file_id):
    download_url = f"{Config.UPLOAD_URL}/download/{file_id}"
    response = requests.get(download_url)

    if response.status_code == 200:
        file_content = BytesIO(response.content)
        return send_file(
            file_content,
            as_attachment=False,
            mimetype="application/pdf",
            download_name=file_id,
        )
    else:
        return jsonify({"message": "File not found"}, 404)
