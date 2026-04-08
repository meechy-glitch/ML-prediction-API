from fastapi import FastAPI 
#from enum import Enum 
from routers import items, users, predictions



#class ModelName(str, Enum):
   # alexnet = "alexnet"
   # resnet = "resnet"
    #lenet = "lenet"


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



#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
#    if model_name is ModelName.alexnet:
#        return {"model_name": model_name, "message": "deep learning FTW!"} 

#    if model_name.value == "lenet":
#        return {"model_name": model_name, "messsage": "LeCNN all the images"}

#    return {"model_name": model_name, "message": "Have some residuals"}



#@app.get("/files/{file_path:path}")
#async def read_file(file_path: str):
#    return {"file_path": file_path}





    