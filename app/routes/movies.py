from flask import Blueprint, request,jsonify
from app.services.movies_services import add_movie,add_details,get_movies,get_details, get_movie_cast,get_movie_with_id, get_movies_by_type,get_video

movies_bp = Blueprint('movies', __name__)
@movies_bp.route('/add-movie', methods=['POST'])
def add_nowplaying_movie():
    allowed_params = ['upcoming', 'top_rated', 'popular', 'now_playing']
    movie_filter = request.args.get('filter')
    if not allowed_params:
        return jsonify({"error": "Missing 'filter' query parameter."}), 400
    if movie_filter not in allowed_params:
        return jsonify({"error":"Invalid parameter"})
    result = add_movie(movie_filter)
    return jsonify(result), result['status']


@movies_bp.route('/add-details', methods=['POST'])
def add_movie_details():
    result = add_details()
    return result

@movies_bp.route('/get-movies', methods=["GET"])
def get_movies_list():
    return get_movies() 
    
@movies_bp.route('/get-movie-details', methods=["GET"])
def get_movies_details():
    return get_details() 

@movies_bp.route('/get-movie-cast', methods=["GET"])
def get_movies_cast():
    return get_movie_cast()

@movies_bp.route('/get-movie-by-id', methods=['GET'])
def get_movie_by_id():
    return get_movie_with_id()

@movies_bp.route('/get-movie-by-type', methods=["GET"])
def get_movie_by_type():
    return get_movies_by_type()

@movies_bp.route('/get-movie-video', methods=["GET"])
def get_movie_video():
    return get_video()

