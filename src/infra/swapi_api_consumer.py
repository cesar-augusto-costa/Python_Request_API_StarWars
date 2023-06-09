from collections import namedtuple
from typing import Dict, Tuple, Type

import requests
from requests import Request

from src.data.interfaces import SwapiApiConsumerInterface
from src.errors import HttpRequestError


class SwapiApiConsumer(SwapiApiConsumerInterface):
    ''' Class to consume swapi with http requests '''

    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')
        self.get_starship_information_response = namedtuple('GET_Starship_Info', 'status_code request response')


    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''
            request starships in pagination
            :param - page: int with page of navegation
            :return - Tuple with status_code, request, response attributes
        '''  
              
        # params = {'page': page}
        # response = requests.get('https://swapi.dev/api/starships/', params=params)
        # return response.json()

        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={"page": page}
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >= 200 and status_code <= 299):
            return self.get_starships_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()['detail'], status_code=status_code
            )
        # print(req.url)
        # print(response.json())


    def get_starship_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        '''
            request starship information
            :param - starship_id: int with id of selected starship
            :return - Tuple with status_code, request, response attributes
        '''  

        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/{}/'.format(starship_id)
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >= 200 and status_code <= 299):
            return self.get_starship_information_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()['detail'], status_code=status_code
            )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        '''
            Prepare a session and send http request
            :param - req_prepared: Request Object with all params
            :response: Htt response raw
        '''
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
    