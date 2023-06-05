from typing import Dict, Type

from src.domain.usecases import StarshipInformationColectorInterface
from src.presenters.interface import ControllersInterface


class StarshipInformationColectorController(ControllersInterface):

    def __init__(self, starship_information_colector: Type[StarshipInformationColectorInterface]) -> None:
        self.__use_case = starship_information_colector

    def handler(self, http_request: Dict):
        ''' Handler to information colector controller '''

        starship_id = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_information = self.__use_case.find_starship(starship_id, time)
