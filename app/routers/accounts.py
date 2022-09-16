from ..database.connection import Session
from ..model.account import Account
from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(prefix="/accounts", tags=["accounts"])


class AccountModel(BaseModel):
    cd_account: int = 0
    cd_user: int = 0
    cd_type: int = 0
    name_account: str = ''
    balance: float = 0.0


@router.get("/")
async def read_account():
    session = Session()
    account = session.query(Account).order_by(Account.name_account).all()
    session.close()

    return account


@router.get("/{cd_account}")
async def read_account(cd_account: str):
    session = Session()
    account = session.query(Account).filter(Account.cd_account == int(cd_account)).first()
    session.close()

    return account


@router.post("/")
async def create_account(account_model: AccountModel):
    new_account = Account(name_account=account_model.name_account, balance=account_model.balance,
                          cd_user=account_model.cd_user, cd_type=account_model.cd_type)
    session = Session()
    session.add(new_account)
    session.commit()
    session.close()

    return Response(status_code=status.HTTP_200_OK, content="created")


@router.put("/")
async def update_account(account_model: AccountModel):
    session = Session()
    account = session.query(Account).filter(Account.cd_account == account_model.cd_account).first()
    if account is not None:
        account.name_account = account_model.name_account
        account.balance = account_model.balance
        account.cd_type = account_model.cd_type
        session.commit()
    session.close()

    return Response(status_code=status.HTTP_200_OK, content="updated")


@router.delete("/")
async def delete_account(account_model: AccountModel):
    session = Session()
    account = session.query(Account).filter(Account.cd_account == account_model.cd_account).first()
    if account is not None:
        session.delete(account)
        session.commit()
    session.close()

    Response(status_code=status.HTTP_200_OK, content="deleted")
