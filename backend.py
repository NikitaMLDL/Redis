import uvicorn
import redis
from fastapi import FastAPI

# инициализация API
app = FastAPI()

# Эндпоинт проверки юзера в БД
@app.get("/check_user/{user_id}")
async def check_user(user_id: int):
    # Подключение к Redis внутри функции для избежания проблемы c pickling
    conn = redis.Redis(ssl=True, host="127.0.0.1", port=6666)
    
    with conn.pipeline() as pipe:
        pipe.get(user_id)
        count = pipe.execute()[0]
    
    return count or 0

if __name__ == "__main__":
    # запуск локального сервера на 127.0.0.1:8000
    uvicorn.run(app, host="127.0.0.1", port=8080)