from fastapi import APIRouter, HTTPException 
from schemas import ItemCreate, ItemResponse
import uuid
import httpx
import asyncio


router = APIRouter(
    prefix="/items",
    tags=["items"]

)


fake_items_db = []


@router.get("/")
async def get_items():
    return fake_items_db


@router.post("/create-item",response_model= ItemResponse)
async def create_item(item: ItemCreate):
    new_item = ItemResponse(
        id = str(uuid.uuid4()),
        **item.model_dump()
    )


    fake_items_db.append(new_item)
    return new_item



@router.get("/external")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
        return response.json()
        


@router.get("/compute")
def heavy_computation():
    result = sum(i * i for i in range(100_000))
    return {"result": result}



@router.post("/predict-async")
async def fake_predict(item: ItemCreate):
    await asyncio.sleep(1)
    return {
        "item": item.name,
        "prediction": "This will be an actual model later"
    }



@router.get("/{item_id}")
async def get_item(item_id: str):
    for item in fake_items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
