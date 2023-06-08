from typing import Union

from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/users")
async def get_users():
	return users

@app.post("/users")
async def create_user(user):
	users.append(user)
	return {"message": "User has been created successfully."}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}