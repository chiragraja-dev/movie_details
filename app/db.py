from flask_pymongo import PyMongo
from pymongo.errors import ServerSelectionTimeoutError

mongo = PyMongo()

def initialize_db(app):

    mongo.init_app(app)
    try:
        mongo.db.list_collection_names()
        print("MongoDB is connected")
    except ServerSelectionTimeoutError as e:
        print(f"Failed to connect to MongoDB: {e}")

def get_db():
    return mongo.db
