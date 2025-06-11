from fastapi import FastAPI
from server_info import data
from controllers import crawlData_controller, inputKeywords_controller

from middlewares import cors_middleware
from middlewares import static_middleware
from middlewares import logging_middleware

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, World!", "server_info": data}

cors_middleware.add(app)
static_middleware.add(app)
logging_middleware.add(app)

app.include_router(crawlData_controller.router)
app.include_router(inputKeywords_controller.router)
