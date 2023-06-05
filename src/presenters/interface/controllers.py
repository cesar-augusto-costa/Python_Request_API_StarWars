from abc import ABC, abstractmethod
from typing import Dict


class ControllersInterface(ABC):
    ''' Interface to Controllers '''

    @abstractmethod
    def handler(self, http_request: Dict):
        ''' Method to handle request '''
        raise 'Should implement handler method'
