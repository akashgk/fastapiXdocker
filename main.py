from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items")
def get_item():
    return {"response": 200, 'items': [{"item1": 1}, {"item2": 2}, {"item3": 3}]}


@app.get("/products")
def get_product():
    return {"response": 200, 'products': [{"item1": 1}, {"item2": 2}, {"item3": 3}]}


@app.get("/softwares")
def get_software():
    return {"response": 200, 'softwares': [{"item1": 1}, {"item2": 2}, {"item3": 3}, {"item4": 4}]}


@app.get("/phones")
def get_software():
    return {"response": 200, 'phones': [{"item1": 1}, {"item2": 2}, {"item3": 3}, {"item4": 4}]}


@app.get("/knives")
def get_knives():
    return {"response": 200, 'knives': [{"item1": 1}, {"item2": 2}, {"item3": 3}, {"item4": 4}]}


@app.get("/cakes")
def get_cakes():
    return {"response": 200, 'cakes': [{"item1": 1}, {"item2": 2}, {"item3": 3}, {"item4": 4}]}


@app.get("/flowers")
def get_cakes():
    return {"response": 200, 'flowers': [{"item1": 1}, {"item2": 2}, {"item3": 3}, {"item4": 4}]}


@app.get("/fruits")
def get_cakes():
    return {"response": 200, 'fruits': [{"item1": 1}, {"item2": 2}, {"item3": 3}, {"item4": 4}]}
