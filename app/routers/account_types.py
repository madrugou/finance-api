from ..database.connection import Session
from ..model.account_type import AccountType
from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(prefix="/account-types", tags=["account-types"])


class AccountTypeModel(BaseModel):
    cd_type: int = 0
    name_type: str = ''


@router.get("/")
async def read_account_types():
    session = Session()
    account_types = session.query(AccountType).order_by(AccountType.name_type).all()
    session.close()

    return account_types


@router.get("/{cd_account_type}")
async def read_account_type(cd_account_type: str):
    session = Session()
    account_type = session.query(AccountType).filter(AccountType.cd_type == int(cd_account_type)).first()
    session.close()

    return account_type


@router.post("/")
async def create_account_type(account_type_model: AccountTypeModel):
    new_account_type = AccountType(name=account_type_model.name_type)
    session = Session()
    session.add(new_account_type)
    session.commit()
    session.close()

    return Response(status_code=status.HTTP_200_OK, content="created")


@router.put("/")
async def update_account_types(account_type_model: AccountTypeModel):
    session = Session()
    account_type = session.query(AccountType).filter(AccountType.cd_type == account_type_model.cd_type).first()
    if account_type is not None:
        account_type.name_type = account_type_model.name_type
        session.commit()
    session.close()

    return Response(status_code=status.HTTP_200_OK, content="updated")


@router.delete("/")
async def delete_category(account_type_model: AccountTypeModel):
    session = Session()
    account_type = session.query(AccountType).filter(AccountType.cd_type == account_type_model.cd_type).first()
    if account_type is not None:
        session.delete(account_type)
        session.commit()
    session.close()

    Response(status_code=status.HTTP_200_OK, content="deleted")
