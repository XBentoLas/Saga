import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SECTRET_KEY = os.getenv("secret_key", "dev_secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DB_TYPE = os.getenv("db_type", "sqlite")
    
    if DB_TYPE == "mysql":
        DB_USER = os.getenv("db_user", "root")
        DB_PASSWORD = os.getenv("db_password", "root")
        DB_HOST = os.getenv("db_host", "localhost")
        DB_PORT = os.getenv("db_port", "3306")
        DB_NAME = os.getenv("db_name", "saga")
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    else:
        INSTANCE_DIR = BASE_DIR / "instance"
        INSTANCE_DIR.mkdir(exist_ok=True)
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{INSTANCE_DIR / 'saga.db'}"