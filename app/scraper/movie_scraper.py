import os
import requests
from dotenv import dotenv_values,load_dotenv

load_dotenv()
tmdb_auth = os.getenv('TMDB_AUTH_KEY')
tmdb_baseurl = os.getenv('TMDB_BASE_URL')
tmdb_account_id= os.getenv('TMDB_ACCOUNT_ID')


class MovieScraper:
    def fetch_movie_dlt(movie_name):
        url = f"{tmdb_baseurl}/search/movie"
        params = {
            'api_key': tmdb_auth,
            'query': movie_name,
            'language': 'en-US'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get('results')
            return results
        return None

   
    def fetch_movie_dltby_id(self,movie_id, page_no=1):
        url = f"{tmdb_baseurl}/movie/{movie_id}"
        
        params = {
            'api_key': tmdb_auth,
            'language': 'en-US',
            'page':page_no
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()
            return results
        else:
            print("Failed to fetch movie:", response.status_code, response.text)



    def fetch_movie_list(self, page_no, region , movie_filter='now_playing'):
        allowed_filters = ['upcoming', 'top_rated', 'popular', 'now_playing']

        if movie_filter not in allowed_filters:
            movie_filter='now_playing'

        url = f"{tmdb_baseurl}/movie/{movie_filter}"

        params = {
            'api_key': tmdb_auth,
            'language': 'en-US',
            'page':page_no,
            'region':region
        }

        if movie_filter == 'popular':
            params.update({
                'sort_by': 'popularity.desc',
                'vote_average.gte': 5
            })

        response = requests.get(url, params)

        if response.status_code == 200:
            movie_lists = response.json()
            return movie_lists
        else:
            return {"status":response.status_code,"msg": response.text}
            # print("Failed to fetch movie lists:", response.status_code, response.text)

        
    def fetch_available_regions():
        url = f"{tmdb_baseurl}/watch/providers/regions"
        params = {
            'api_key': tmdb_auth,
            'language': 'en-US'
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            regions = data['results']

            for region in regions:
                print(f"Country Code: {region['iso_3166_1']}, Region Name: {region['english_name']}")
        else:
            print("Failed to fetch data:", response.status_code)


    def fetch_movie_cast(self, movie_id):
        url = f"{tmdb_baseurl}/movie/{movie_id}/credits"
        params = {
            'api_key': tmdb_auth,
            'language': 'en-US'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()
            return results
        else:
            print("Failed to fetch movie:", response.status_code, response.text)


    def fetch_movie_videos(self,movie_id):
        url = f"{tmdb_baseurl}/movie/{movie_id}/videos"
        params = {
            'api_key': tmdb_auth,
            'language': 'en-US'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()
            return results
        else:
            print("Failed to fetch movie:", response.status_code, response.text)

    def scrap_all_pages(self, filter_data='now_playing'):
        page_no = 1
        movie_data = []
        region = 'IN'
        scrap_data_init = self.fetch_movie_list(page_no, region, filter_data)
        no_of_pages = scrap_data_init.get('total_pages', 1)

        if filter_data == 'popular':
            no_of_pages = min(no_of_pages, 10000)

        movie_data.extend(scrap_data_init.get('results', []))

        for i in range(2, no_of_pages + 1):
            print(f"Fetching page {i}/{no_of_pages}...")
            scrap_data_init = self.fetch_movie_list(i, region, filter_data)
            movie_data.extend(scrap_data_init.get('results', []))

        return movie_data



                        















# MovieScraper.fetch_movie_list(1, "IN")
# MovieScraper.fetch_movie_dltby_id(872906)
# MovieScraper.fetch_movie_cast(872906)
# MovieScraper.fetch_movie_videos(872906)
# MovieScraper.fetch_available_regions()