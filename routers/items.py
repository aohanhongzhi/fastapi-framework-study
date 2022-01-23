from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from pydantic import BaseModel
from typing import Optional

from dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/list")
async def read_items_list():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}

@router.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


@router.get("/items/{item_id}")
def read_item(item_id: int = 1, q: Optional[str] = None):
    """
    :param item_id: 默认值为 1
    :param q: 可选参数，默认值为 None
    :return:
    """
    logger.debug("\n====>输入参数是{},{}", item_id, q)
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """
    可以用对象来接收参数
    :param item_id:
    :param item: 参数通过request body 传输过来，使用json
    :return:
    """
    return item