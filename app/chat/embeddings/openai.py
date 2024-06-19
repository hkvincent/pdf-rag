import os
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_EMBEDDING_KEY"),
    openai_api_base=os.getenv("OPENAI_EMBEDDING_BASE_URL"),
)
