from langchain.schema import HumanMessage
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models.gigachat import GigaChat


class StreamHandler(BaseCallbackHandler):
    def __init__(self, initial_text=""):
        pass

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # print(f"{token} -", end="", flush=True)
        print(f"{token}", end="", flush=True)


chat = GigaChat(credentials='OTVkNjA0MGMtNjY4OS00MDBiLWJjOTUtYzcyMGI3ZjU4MjZlOmYwYTZkZmY1LTgyYjUtNDYxMS04ZmI3LWFmZDI0YmVjMWJhYg==',
                streaming=True,
                callbacks=[StreamHandler()],
                verify_ssl_certs=False)

chat([HumanMessage(content="Напиши краткое содержание романа 'Евгений Онегин'. Длина текста около 2000 символов")])
