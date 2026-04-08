from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserResponse
import uuid


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


fake_users_db = []


@router.get("/")
async def get_users():
    return fake_users_db



@router.post("/create-user", response_model=UserResponse)
async def create_user(user: UserCreate):
    new_user = UserResponse(
        id = str(uuid.uuid4()),
        **user.model_dump()
    )

    fake_users_db.append(new_user)
    return new_user



@router.get("/{user_id}")
async def get_user(user_id: str):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
