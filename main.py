import time
import pysnooper
import uvicorn
from fastapi import FastAPI
from loguru import logger

app = FastAPI()


@app.get("/")
@pysnooper.snoop()  # 这个必须贴近下面方法名
def read_root():
    logger.debug("====>访问fastapi首页")

    # 测试线程并发度 经过多番测试大概并发度一般是 CPU核心数+1
    time.sleep(4)
    return {"Hello": "World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    logger.debug("\n====>输入参数是{},{}", item_id, q)
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    logger.debug("程序开始启动")
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
