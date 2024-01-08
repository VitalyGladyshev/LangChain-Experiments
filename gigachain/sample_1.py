from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(
    credentials='OTVkNjA0MGMtNjY4OS00MDBiLWJjOTUtYzcyMGI3ZjU4MjZlOmYwYTZkZmY1LTgyYjUtNDYxMS04ZmI3LWFmZDI0YmVjMWJhYg==', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты специалист по созданию продуктов на основе большой языковой модели GigaChat"
    )
]

while (True):
    # Ввод пользователя
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    # Ответ сервиса
    print("Bot: ", res.content)
