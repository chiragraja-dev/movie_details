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


class MoviesDetails:
    def __init__(
        self,
        adult,
        backdrop_path,
        belongs_to_collection,
        budget,
        genres,
        homepage,
        id,
        imdb_id,
        origin_country,
        original_language,
        original_title,
        overview,
        popularity,
        poster_path,
        production_companies,
        production_countries,
        release_date,
        revenue,
        runtime,
        spoken_languages,
        status,
        tagline,
        title,
        video,
        vote_average,
        vote_count
    ):
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.belongs_to_collection = belongs_to_collection
        self.budget = budget
        self.genres = genres
        self.homepage = homepage
        self.id = id
        self.imdb_id = imdb_id
        self.origin_country = origin_country
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.production_companies = production_companies
        self.production_countries = production_countries
        self.release_date = release_date
        self.revenue = revenue
        self.runtime = runtime
        self.spoken_languages = spoken_languages
        self.status = status
        self.tagline = tagline
        self.title = title
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count

    def to_dict(self):
        return self.__dict__



class MoviesCast:
    def __init__(self, id, cast, crew):
        self.id = id
        self.cast = [CastMember(**member) for member in cast] if cast else []
        self.crew = [CrewMember(**member) for member in crew] if crew else []

    def to_dict(self):
        return {
            "id": self.id,
            "cast": [member.to_dict() for member in self.cast],
            "crew": [member.to_dict() for member in self.crew]
        }

class CastMember:
    def __init__(self, adult, gender, id, known_for_department, name, original_name,
                 popularity, profile_path, cast_id, character, credit_id, order):
        self.adult = adult
        self.gender = gender
        self.id = id
        self.known_for_department = known_for_department
        self.name = name
        self.original_name = original_name
        self.popularity = popularity
        self.profile_path = profile_path
        self.cast_id = cast_id
        self.character = character
        self.credit_id = credit_id
        self.order = order

    def to_dict(self):
        return self.__dict__

class CrewMember:
    def __init__(self, adult, gender, id, known_for_department, name, original_name,
                 popularity, profile_path, credit_id, department, job):
        self.adult = adult
        self.gender = gender
        self.id = id
        self.known_for_department = known_for_department
        self.name = name
        self.original_name = original_name
        self.popularity = popularity
        self.profile_path = profile_path
        self.credit_id = credit_id
        self.department = department
        self.job = job

    def to_dict(self):
        return self.__dict__

class MoviesVideo:
    def __init__(self, id,results):
        self.id= id
        self.results = [VideoInfo(**data) for data in results]
    def to_dict(self):
        return{
            "id":self.id,
            "results": [member.to_dict() for member in self.results]
        }

class VideoInfo:
    def __init__(self, iso_639_1, iso_3166_1, name, key, site, size, type, official, published_at, id):
        self.iso_639_1 = iso_639_1
        self.iso_3166_1 = iso_3166_1
        self.name = name
        self.key = key
        self.site = site
        self.size = size
        self.type = type
        self.official = official
        self.published_at = published_at
        self.id = id

    def to_dict(self):
        return {
            "iso_639_1": self.iso_639_1,
            "iso_3166_1": self.iso_3166_1,
            "name": self.name,
            "key": self.key,
            "site": self.site,
            "size": self.size,
            "type": self.type,
            "official": self.official,
            "published_at": self.published_at,
            "id": self.id
        }

# class 