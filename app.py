from fastapi import FastAPI
from api import endpoints

def api_endpoints(app:FastAPI) -> FastAPI:
    app.include_router(endpoints.router)
    return app

def create_app() -> FastAPI:
    """create and return fastapi app"""
    app = FastAPI()
    app = api_endpoints(app)
    return app

app = create_app()
