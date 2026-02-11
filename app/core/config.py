import os

class Settings:
    APP_NAME: str = "Task Service"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///:memory:")

settings = Settings()
