from app.db import get_db
from app.models.movie_schemas import Movies, MoviesDetails, MoviesCast, MoviesVideo
from app.scraper.movie_scraper import MovieScraper
from datetime import datetime
from bson.json_util import dumps, loads
from flask import request,jsonify  
from bson import ObjectId

def add_movie(filter_type):
    try:
        db=get_db()
        scraper = MovieScraper()
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


def add_details():
    try:
        db= get_db()
        movies= db.movies.find({"filter_type": "popular"})
        movies_list = loads(dumps(movies))
        scraper= MovieScraper()
        movie_dlt=[]
        for movie in movies_list:
            movie_id = movie['id']
            resullt = scraper.fetch_movie_dltby_id(movie_id)
            movie_dlt.append(resullt)

        movie_dlt = [MoviesDetails(**movie).to_dict() for movie in movie_dlt]
        db.movies_details.insert_many(movie_dlt)
        return {"status":200, "message":"Added"}
    except Exception as e:
        return {"status":500, "message":"Internal server error", "details": str(e)}

def get_movies():
    try:
        db=get_db()
        page = request.args.get('page',1,type=int)
        limit = 40
        skip = (page-1) * limit

        movie_list_undump = list(db.movies.find().skip(skip).limit(limit).sort([("_id",1)]))
        movies_list =convert_objectid(movie_list_undump)
        total_count = db.movies.count_documents({})
        total_pages = (total_count + limit -1)//limit
        response= {
            "status":200,
            "data":movies_list,
            "pagination": {
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "page_limit": limit
            }
        }
        return jsonify(response)
    except Exception as e:

        return {"status":500,"message":"Internal server error","details": str(e)}

def convert_objectid(data):
    if isinstance(data, list):
        return [convert_objectid(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_objectid(value) for key, value in data.items()}
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data
       
def convert_objectid_for_id(data):
    return [{**doc, "_id": str(doc["_id"])} for doc in data]

def get_details():
    try:
        db = get_db()
        id = request.args.get('id',1,type=int)
        data = db.movies_details.find_one({"id":id})
        data_for_id = convert_objectid(data)
        
        if data_for_id:
            return {"status":200, "data":data_for_id}
        else:
            scraper = MovieScraper()
            resullt = scraper.fetch_movie_dltby_id(id)
            if isinstance(resullt, MoviesDetails):
                movie_details_dict = resullt.to_dict()
            else:
                movie_details_dict = resullt
            insert_result = db.movies_details.insert_one(movie_details_dict)
            inserted_document = db.movies_details.find_one({"_id": insert_result.inserted_id})
            data = convert_objectid(inserted_document)
            return {"status":200, "data":data}
    except Exception as e:
            return {"status":500,"message":"Internal server error","details": str(e)}


def get_movie_cast():
    try:
        db= get_db()
        id = request.args.get('id',1,type=int)
        data = db.movie_cast.find_one({"id":id})
        data_for_id = convert_objectid(data)

        if data_for_id:
            add_movie_video(id)
            return {"status":200,"data":data_for_id}
        else:
            scraper = MovieScraper()
            add_movie_video(id)
            result = scraper.fetch_movie_cast(id)
            if isinstance(result, MoviesCast):
                movie_details_dict = result.to_dict()
            else:
                movie_details_dict= result
            insert_result = db.movie_cast.insert_one(movie_details_dict)
            insert_doc = db.movie_cast.find_one({"_id":insert_result.inserted_id})
            data = convert_objectid(insert_doc)
            return {"status":200, "data":data}
    except Exception as e:
        return {"status":500,"message":"Internal server error","details": str(e)}


def add_movie_video(id):
    db= get_db()
    scraper = MovieScraper()
    movie= db.movie_video.find_one({"id":id})
    if movie:
        print("data already present")
    else:
        result = scraper.fetch_movie_videos(id)
        if isinstance(result, MoviesVideo):
            movie_video_dict = result.to_dict()
        else:
            movie_video_dict= result
        insert_result = db.movie_video.insert_one(movie_video_dict)
        print("data added")

def get_movie_with_id():
    try:
        db = get_db()
        id = request.args.get('id',1,type=int)
        data = db.movies.find_one({"id":id})
        movies_list =convert_objectid(data)
        return {"status":200, "message":movies_list}
    except Exception as e:
        return {"status":500,"message":"Internal server error","details": str(e)}

def get_movies_by_type():
    try:
        db = get_db()
        movie_type = request.args.get('type',  default="now_playing", type=str)
        page = request.args.get('page',default=1, type=int)
        if page > 1:
             return {"status":400, "message":"Page number can't be zero or negative"}
        movie_type = movie_type.strip().lower()
        data_types = ["now_playing","upcoming","top_rated","popular"]
      
        if movie_type in data_types:
            page_size = 40
            skip_count= (page-1) * page_size
            data = db.movies.find({"filter_type":movie_type}).skip(skip_count).limit(page_size).sort([("_id",1)])

            total_count = db.movies.count_documents({"filter_type":movie_type})

            total_pages = (total_count + page_size -1)//page_size

            movies_list = convert_objectid_for_id(data)
            return {
                "status":200,
                "data":movies_list,
                "pagination": {
                "current_page": page,
                "total_pages": total_pages,
                "total_items": total_count,
                "page_page_size": page_size
            }
                 }
        else:
            return {"status":400, "message":"wrong parameter"}
        
    except Exception as e:
        return {"status":500,"message":"Internal server error","details": str(e)}


def get_video():
    try:
        db = get_db()
        id = request.args.get('id',1,type=int)
        data = db.movie_video.find_one({"id":id})
        movie_video =convert_objectid(data)
        return {"status":200, "message":movie_video}
    except Exception as e:
        return {"status":500,"message":"Internal server error","details": str(e)}

