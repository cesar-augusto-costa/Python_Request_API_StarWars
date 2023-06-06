from cerberus import Validator


def get_pagination_validator(request: any):
    ''' pagination validator '''

    query_param_validator = Validator({
        'page': {
            'type': 'string',
            'allowed': ['1', '2', '3', '4'],
            'required': True
        }
    })

    response = query_param_validator.validate(request.query_params)   
    # print(query_param_validator.errors)
    # print(response)

    if response is False:
        raise Exception(query_param_validator.errors)
    