from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type

from requests import Request


class SwapiApiConsumerInterface(ABC):
    ''' Api Consumer Interface'''

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_starships')
    
    @abstractmethod
    def get_starships_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_starships_information')
    
