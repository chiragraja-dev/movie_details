import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY=os.getenv("DB_SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI")