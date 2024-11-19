from app.db import get_db
from app.models.movie_schemas import Movies
from app.scraper.movie_scraper import MovieScraper
from datetime import datetime

def add_movie(filter_type):
    try:
        db=get_db()
        scraper = MovieScraper()
        print(db.list_collection_names())
        movie_data = scraper.scrap_all_pages(filter_type)
        additional_fields = {
            "filter_type": filter_type,
            "region": "IN",
            "scraped_at": datetime.utcnow()  
        }
        data = [Movies(**movie).to_dict() | additional_fields for movie in movie_data]
        db.movies.insert_many(data)
        return {"status":200, "message":"list is added successfull"}
    except Exception as e:
        return {"status":500, "message":"Internal server error"}

# def add_details():
#     try:
#         db = get_db()
    
