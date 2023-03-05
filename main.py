
from dotenv import load_dotenv

from backend.meu_app_backend.utils.constants import ENV
load_dotenv()

import os
from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    if (ENV == 'prod'):
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=80,
                    reload=True,
                    ssl_keyfile="certs/fullchain.pem",
                    ssl_certfile="certs/cert.pem"
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )