class Movies:
    def __init__(self, adult, backdrop_path, genre_ids, id, original_language, 
                 original_title, overview, popularity, poster_path, release_date, 
                 title, video, vote_average, vote_count):
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.genre_ids = genre_ids
        self.id = id
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.release_date = release_date
        self.title = title
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count

    def to_dict(self):
        return self.__dict__