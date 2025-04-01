import requests
#from urllib.parse import urlencode

class CosmicJsApi:
    def __init__(self, bucket_slug, read_key, write_key):
        self.base_url = f"https://api.cosmicjs.com/v3/buckets/{bucket_slug}"
        self.read_key = read_key
        self.write_key = write_key

    def get_movies(self):
        url = f'{self.base_url}/objects?1=1&query=%7B"type":"movies"%7D'
        params = {
            'read_key': self.read_key,
            'limit': 100
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get('objects', [])
        else:
            if response.status_code == 404:
                return []
            else:
                response.raise_for_status()

    def movie_exists(self, slug):
        from urllib.parse import quote
        query = quote(f'{{"type": "movies", "slug": "{slug}"}}')
        url = f"{self.base_url}/objects?query={query}"
        params = {
            'read_key': self.read_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return True
        else:
            return False
            
    def add_movie(self, title, slug, content):
        if self.movie_exists(slug):
            return f"Movie {slug} already exists"
        
        url = f"{self.base_url}/objects"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.write_key}'
        }
        data = {
            'title': title,
            'slug': slug,	
            'type': 'movies',
            
            'metadata': { 'movieattributes' : content }
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
            
            
if __name__ == '__main__':
    
    # read the keys from localvar.py
    import localvar as lv
    COSMIC_BUCKET_SLUG = lv.COSMIC_BUCKET_SLUG
    COSMIC_READ_KEY = lv.COSMIC_READ_KEY
    COSMIC_WRITE_KEY = lv.COSMIC_WRITE_KEY
    '''
    cosmicjs = CosmicJsApi(COSMIC_BUCKET_SLUG, COSMIC_READ_KEY, COSMIC_WRITE_KEY)
    
    print(cosmicjs.get_movies())
    print(cosmicjs.movie_exists('sujo-111'))
    
    content = {'title' : 'titel', 'description': 'omschrijving', 'directors': 'Hitchcock', 'count': 0, 'reviewTotal':0 }
        
    r = cosmicjs.add_movie('titel 1', 'titel-1', content)
    
    print(r)
    print(cosmicjs.get_movies())

    '''	