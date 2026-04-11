from fastapi import FastAPI 
from routers import items, users, predictions


app = FastAPI()


app.include_router(items.router)
app.include_router(users.router)
app.include_router(predictions.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my first api endpoint"}


@app.get("/health")
async def health_status():
    return {"status": "okay"}

    