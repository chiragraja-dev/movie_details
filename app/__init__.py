from flask import Flask
from app.routes import add_movie

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    add_movie(app)
    return app
