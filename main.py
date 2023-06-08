from typing import Optional, Union, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
	email: str
	is_active: bool
	bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
	return users


@app.post("/users")
async def create_user(user: User):
	users.append(user)
	return {"message": "User has been created successfully."}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}
