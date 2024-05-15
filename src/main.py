from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from server.client import service as client_service
from server.client.client import Client

app = FastAPI()

@app.get("/")
def read_root():
    return {"Empty"}

@app.post("/create/client", status_code=200)
def create_client(data: Client, response: JSONResponse):
    print(data)
    try:
        message = client_service.create_client(data)
    except HTTPException as err:
        if err.status_code == 409:
            response.status_code = 409
            message = {"info": "Client already exists"}
    else:
        response.status_code = 200
    return message
