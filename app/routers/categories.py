from ..controller.categoryController import CategoryController
from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(prefix="/categories", tags=["categories"])

categoryController = CategoryController()


class CategoryModel(BaseModel):
    cd_category: int = 0
    name_category: str = ''


@router.get("/")
async def read_categories():
    categories = categoryController.read_categories()
    return categories


@router.get("/{cd_category}")
async def read_category(cd_category: str):
    category = categoryController.read_category_by_id(cd_category)
    return category


@router.post("/")
async def create_category(category_model: CategoryModel):
    new_category = categoryController.create_category(category_model)
    return Response(status_code=status.HTTP_200_OK, content="created")


@router.put("/")
async def update_category(category_model: CategoryModel):
    category = categoryController.update_category(category_model)
    return Response(status_code=status.HTTP_200_OK, content="updated")


@router.delete("/")
async def delete_category(category_model: CategoryModel):
    category = categoryController.delete_category(category_model)
    Response(status_code=status.HTTP_200_OK, content="deleted")
