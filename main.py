from typing import Optional, Union, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
		title="FastAPI Tutorial LMA",
		description="LMA for managing students and courses",
		version="1.0.0",
		contact={
			"name" : "Cristian",
			"email": "email@example.com",
		},
		license_info={
			"name": "Apache 2.0",
		}
)

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


@app.get("/users/{id}")
async def get_user(
		id: int = Path(..., description="The ID of the user to get."),
		q: str = Query(None, max_length=5)
):
	return {"user": users[id], "q": q}
