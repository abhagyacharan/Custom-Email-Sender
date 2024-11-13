# backend/app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Email Sender MVP"
    DATABASE_URL: str = "postgresql://user:password@localhost/email_sender"
    REDIS_URL: str = "redis://localhost:6379/0"
    SENDGRID_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    EMAIL_SENDER: str = "noreply@yourdomain.com"
    
    # Email sending limits
    MAX_EMAILS_PER_HOUR: int = 100
    MAX_EMAILS_PER_DAY: int = 1000
    
    class Config:
        env_file = ".env"

settings = Settings()

# backend/app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()