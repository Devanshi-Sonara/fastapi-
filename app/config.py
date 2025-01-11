from pydantic_settings import BaseSettings
# Explicitly load the .env file

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = {
        "env_file": "F:\fastapi_practice\.env"  # Specify the path to your .env file here
    }

settings = Settings()

