from fastapi import APIRouter
from fastapi import Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.main.adapters import request_adapter
from src.main.composer import (get_starship_information_composer,
                               get_starships_in_pagination_composer)
from src.presenters.errors import handle_errors
from src.validators import (get_pagination_validator,
                            get_starship_information_validator)

starships_routes = APIRouter()

@starships_routes.get('/api/starships/list')
async def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''

    response = None
    controller = get_starships_in_pagination_composer()

    try:
        get_pagination_validator(request)
        response = await request_adapter(request, controller.handle)
    except Exception as error:
        response = handle_errors(error)

    # print(request.query_params)
    # print(request.query_params['page'])
    # return { 'Ola': 'Mundo' }

    return JSONResponse(
        status_code=response['status_code'],
        content=response['data']
        # content={'data': response['data']}
    )

# Essa rota poderia ser com GET
@starships_routes.post("/api/starships/information")
async def get_starship_information(request: RequestFastApi):
    ''' get_starship_information '''

    response = None
    controller = get_starship_information_composer()

    try:
        await get_starship_information_validator(request)
        response = await request_adapter(request, controller.handler)
    except Exception as error:
        response = handle_errors(error)    

    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )

