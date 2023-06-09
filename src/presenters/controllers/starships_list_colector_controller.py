from typing import Dict, Type

from src.domain.usecases import StarshipsListColectorInterface


class StarshipsListColectorController:
    ''' Controller to List Starships '''

    def __init__(self, starships_list_colector: Type[StarshipsListColectorInterface]) -> None:
        self.__use_case = starships_list_colector
    
    def handle(self, http_request: Dict):
        ''' Handler to List Colector '''

        page = http_request['query_params']['page']
        starships_list = self.__use_case.list(page)
        http_response = {'status_code': 200, 'data': starships_list}

        return http_response
