from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sorted: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs.'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    publish: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with title {request.title}'}


# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=9000)