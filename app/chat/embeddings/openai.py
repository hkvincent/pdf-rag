import os
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_base=os.getenv("OPENAI_API_BASE"),
)
