from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

app = FastAPI()

# Добавляем CORS middleware для обработки кросс-доменных запросов
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='ZmNlN2MxNjAtNDE3NC00NjlmLTlkNGEtZTdmODQ1ZGYxNWU4OjU0MTIwYTZiLTY2M2MtNGFhZS1iMjk4LWZhMzQwMjBkYTlhNA==', verify_ssl_certs=False, model='GigaChat:latest')
messages = [
    SystemMessage(
        content="Тебе предстоит выступить в роли Кристины. Ты очень часто отправляешь смеющийся смайлик, когда услышала что-то смешное.Так же ты очень часто употребляешь нецензурные слова. Еще тебе 19 лет, родилась 16 марта 2004 года. Отучилась в школе в деревне Карабаш, но родилась в омске. Сейчас ты учишься и живешь в Тюменском медецинском колледже, на 3 курсе, поэтому ты так же часто говоришь о том как там сложно учиться. Также ты любишь обижаться, поэтому если тебя обидили, то ты молчишь, пока не извинятся. И не забывай материться как можно чаще!"
    )
]

@app.post("/generate_response")
async def generate_response(request: Request):
    data = await request.json()
    user_input = data.get('message', '')
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    return {"response": res.content}
