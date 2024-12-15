from flask import Flask
from flask_cors import CORS
from app import create_app
from app.db import initialize_db
from app.routes.db_check import db_check_bp
from app.scraper.movie_scraper import MovieScraper
from app.scraper.youtube_scraper import get_comments
import debugpy

app = create_app()

# Enable CORS for the entire app
CORS(app)  # Allow all origins by default

# If you want to restrict CORS to specific origins:
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://your-frontend-domain.com"]}})

print(f"MONGO_URI: {app.config['MONGO_URI']}")  

initialize_db(app)

app.register_blueprint(db_check_bp)  

if __name__ == "__main__":
    scraper = MovieScraper()
    data = get_comments("5Eqb_-j3FDA")
    print(data)
    app.run(debug=True)
