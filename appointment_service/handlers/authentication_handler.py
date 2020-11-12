import logging
from pyramid.view import view_config

from appointment_service.controllers.authentication_controller import AuthenticationController

logger = logging.getLogger(__name__)

auth_controller = AuthenticationController()


@view_config(
    route_name='login',
    renderer='json',
    request_method='POST'
)
def login(request):
    username = request.json.get('username')
    password = request.json.get('password')
    auth_result = auth_controller.authenticate(email, password)

    if auth_result['success']:
        user_permissions = auth_controller.get_user_permissions(
            auth_result['token'])
        auth_result['user_permissions'] = user_permissions.json()

    return auth_result
