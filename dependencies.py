from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(...)):
    """
    检查全局的token信息
    :param x_token:
    :return:
    """
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    """
    全局检查是否存在
    :param token:
    :return:
    """
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
