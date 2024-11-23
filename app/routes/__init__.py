from app.routes.movies import movies_bp

def add_movie(app):
    app.register_blueprint(movies_bp, url_prefix='/')

# def add_details(app):
#     app.register_blueprint(movies_bp, url_prefix='/')