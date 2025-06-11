from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    PORT: int
    DB_HOST: str  
    DB_PORT: int 
    DB_USER: str 
    DB_NAME: str 
    DB_PASSWORD: str  
    JWT_SECRET_KEY: str
    TOKEN_LIFETIME: str
    REFRESH_TOKEN_KEY: str
    REFRESH_TOKEN_LIVETIME: str 

    class Config:
        env_file = ".env"

settings = Settings()