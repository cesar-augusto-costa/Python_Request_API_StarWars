import requests


class SwapiApiConsumer:
    
    @classmethod
    def get_starships(self, page: int) -> any:
        ''' Testing get_starships method '''

        params = {'page': page}
        response = requests.get('https://swapi.dev/api/starships/', params=params)

        return response.json()
