from .dependencies import get_token_header
from fastapi import Depends, FastAPI
from .environment import configuration
from datetime import datetime
from .database.connection import engine,  Base
from .routers import users, categories, account_types, accounts

Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_token_header)])
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(account_types.router)
app.include_router(accounts.router)

start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get("/status")
async def status():

    status_api = {
        'api-name': configuration["api-name"],
        'version': configuration["api-version"],
        'started': start_time,
        'updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    return status_api
