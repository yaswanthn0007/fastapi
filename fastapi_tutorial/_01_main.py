import json
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    BooksData = open('C:/Users/Yaswanth/PycharmProjects/bookstore/books.json').read()
    data = json.loads(BooksData)

    return {'data': data}


@app.get("/blogs")
def blogs(limit, published):
    return {'data': f"{limit} blogs where published = {published}"}


@app.get("/blog/{id:int}")
def show(id: int):
    return {'data': id}


@app.get("/blog/{id}")
def show2(id: str):
    return {'data2': id}


@app.get("/blog/comments")
def show():
    return {'data': {2: {'comments'}}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    return {'data': f"Blog title : {request.title}"}




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
