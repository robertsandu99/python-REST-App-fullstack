from fastapi import FastAPI
from api import endpoints
from fastapi.middleware.cors import CORSMiddleware

def api_endpoints(app:FastAPI) -> FastAPI:
    app.include_router(endpoints.router)
    return app

def create_app() -> FastAPI:
    """create and return fastapi app"""
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins; for production, specify frontend URL
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )

    app = api_endpoints(app)
    return app

app = create_app()
