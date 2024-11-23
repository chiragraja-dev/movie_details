from flask import Blueprint, request,jsonify
from app.services.movies_services import add_movie,add_details,get_movies,get_details, get_movie_cast

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