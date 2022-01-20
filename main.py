import time

from fastapi import FastAPI
from loguru import logger
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    logger.debug("====>访问fastapi首页")
    time.sleep(9)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    logger.debug("\n====>输入参数是{},{}", item_id, q)
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    logger.debug("程序开始启动")
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
