import os
from langchain.chat_models import ChatOpenAI


def build_llm(chat_args, model_name):
    return ChatOpenAI(
        streaming=chat_args.streaming,
        model_name=model_name,
        baseopenai_api_base_url=os.getenv("OPENAI_API_BASE"),
    )
