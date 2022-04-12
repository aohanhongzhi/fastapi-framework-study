import time
from concurrent.futures.thread import ThreadPoolExecutor

import pysnooper
import uvicorn
from fastapi import FastAPI, Query, status, Depends
from loguru import logger

from dao import models
from dao.database import engine
from routers import users, items
from dependencies import get_token_header

# 创建一个包含3条线程的线程池
pool = ThreadPoolExecutor(max_workers=3)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_token_header)])

# 路由注册
app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
@pysnooper.snoop()  # 这个必须贴近下面方法名
def read_root():
    logger.debug("====>访问fastapi首页")

    # 测试线程并发度 经过多番测试大概并发度一般是 CPU核心数+1
    time.sleep(4)
    return {"Hello": "World"}


@app.get("/hello/{name}")
async def say_hello(name: str = Query(None, max_length=50)):
    """

    :param name:  查询参数校验，最大长度为50
    :return:
    """
    return {"message": f"Hello {name}"}


@app.get("/exception_catch", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
@logger.catch
def exception_catch():
    raise RuntimeError("loguru异常捕获")


@app.get("/exception_catch2")
@logger.catch
def exception(x: int):
    try:
        return 1 / x
    except ZeroDivisionError:
        logger.exception("What?!")


@app.on_event("startup")
async def startup_event():
    """
    这个方法相当于SpringBoot的@PostConstruct，随着SpringBoot启动完成就初始化。
    这里放一些mq之类的启动了！！
    :return: https://fastapi.tiangolo.com/zh/advanced/events/
    """
    logger.info("在fastapi的程序就绪之前启动完成！")
    pool.submit(mq_start)


def mq_start():
    logger.info("开启消息监听")


if __name__ == '__main__':
    logger.debug("程序开始启动")
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
