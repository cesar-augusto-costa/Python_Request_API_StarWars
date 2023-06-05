from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipInformationColectorInterface(ABC):
    ''' Starships Information Colector Interface '''

    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        ''' Must implement '''
        raise Exception('Must implement list method')
