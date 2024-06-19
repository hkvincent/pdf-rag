from langfuse.model import CreateTrace
from app.chat.tracing.langfuse import langfuse


class TraceableChain:
    def __call__(self, *args, **kwargs):
        trace = langfuse.trace(
            CreateTrace(id=self.metadata["conversation_id"], metadata=self.metadata)
        )
        callbacks = kwargs.get("callbacks", [])
        print(
            "Before appending, callbacks is:", callbacks
        )  # Debug statement to check the value of callbacks
        if callbacks is None:
            callbacks = []  # Ensure callbacks is always a list
            print("Callbacks was None, initialized to empty list.")
        callbacks.append(trace.getNewHandler())
        kwargs["callbacks"] = callbacks

        return super().__call__(*args, **kwargs)
