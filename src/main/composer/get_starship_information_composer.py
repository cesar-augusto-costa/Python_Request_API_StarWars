from src.data.usescases import StarshipInformationColector
from src.infra import SwapiApiConsumer
from src.presenters.controllers import StarshipInformationColectorController


def get_starship_information_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipInformationColector(infra)
    controller = StarshipInformationColectorController(usecase)

    return controller


