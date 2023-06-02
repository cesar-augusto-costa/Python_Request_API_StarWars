from fastapi import APIRouter
from fastapi import Request as RequestFastApi

from src.validators.get_starships_in_pagination_validator import \
    get_pagination_validator

starships_routes = APIRouter()

@starships_routes.get('/api/starships/list')
def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''


    print(request.query_params)
    print(request.query_params['page'])
    return { 'Ola': 'Mundo' }
