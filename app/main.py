from fastapi import FastAPI
from app.api.tasks import router as task_router

def create_app() -> FastAPI:
    """
    Application factory.
    Creates and configures the FastAPI app.
    """
    app = FastAPI(
        title="DevOps Task Service",
        description="Backend service to manage real DevOps tasks",
        version="1.0.0",
    )

    # Register API routers
    app.include_router(task_router, prefix="/api")

    return app

app = create_app()
