from langchain.chat_models import ChatOpenAI

def build_llm(chat_args, model_name):
    return ChatOpenAI(
        streaming=chat_args.streaming,
        model_name=model_name,
        base_url = "https://burn.hair/"  # Example base URL for the API
    )
