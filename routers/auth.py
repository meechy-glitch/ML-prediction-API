from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token, verify_token
import bcrypt

router = APIRouter(
    prefix="/auth", 
    tags=["auth"]
)

hashed_password = bcrypt.hashpw("password123".encode("utf-8"), bcrypt.gensalt())

FAKE_USER = {
    "username": "mitchell",
    "hashed_password": hashed_password
}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    submitted_username = form_data.username.lower()
    username_match = submitted_username == FAKE_USER["username"]
    password_match = bcrypt.checkpw(form_data.password.encode("utf-8"), FAKE_USER["hashed_password"])

    if not username_match or not password_match:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token(data={"sub": submitted_username})
    return {"access_token": token, "token_type": "Bearer"}


@router.get("/me")
async def get_current_user(payload: dict = Depends(verify_token)):
    return {
        "username": payload.get("sub"),
        "message": "Token is valid"
    }