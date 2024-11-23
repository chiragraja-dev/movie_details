from app import create_app
from app.db import initialize_db
from app.routes.db_check import db_check_bp
from app.scraper.movie_scraper import MovieScraper
import debugpy

app = create_app()

print(f"MONGO_URI: {app.config['MONGO_URI']}")  # Verify that MONGO_URI is being loaded

initialize_db(app)

if __name__ == "__main__":
    scraper = MovieScraper()
    # scraper.fetch_movie_videos(872906)
    app.run(debug=True)
