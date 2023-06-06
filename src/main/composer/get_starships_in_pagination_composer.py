from src.data.usescases import StarshipsListColector
from src.infra import SwapiApiConsumer
from src.presenters.controllers import StarshipsListColectorController


def get_starships_in_pagination_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipsListColector(infra)
    controller = StarshipsListColectorController(usecase)

    return controller


