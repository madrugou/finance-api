from ..controller.userController import UserController
from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])
userController = UserController()


class UserModel(BaseModel):
    cd_user: int = 0
    name_user: str = ''
    email_user: str = ''
    password: str = ''


@router.get("/")
async def read_users():
    users = userController.read_users()
    return users


@router.get("/{cd_user}")
async def read_user(cd_user: str):
    user = userController.read_user_by_id(cd_user)
    return user


@router.post("/")
async def create_user(user_model: UserModel):
    user = userController.create_user(user_model)
    return Response(status_code=status.HTTP_200_OK, content="created")


@router.put("/")
async def update_user(user_model: UserModel):
    user = userController.update_user(user_model)
    return Response(status_code=status.HTTP_200_OK, content="updated")


@router.delete("/")
async def delete_user(user_model: UserModel):
    user = userController.delete_user(user_model)

    return Response(status_code=status.HTTP_200_OK, content="deleted")
