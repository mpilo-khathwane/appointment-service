import logging
import pyramid.httpexceptions as exc

from pyramid.security import NO_PERMISSION_REQUIRED
from appointment_service.controllers.authentication_controller import AuthenticationController

logger = logging.getLogger(__name__)


def authorization_view(view, info):
    view_permission = info.options.get('permission')
    if view_permission and view_permission != NO_PERMISSION_REQUIRED:
        def wrapper_view(context, request):

            authorization = request.headers.get('Authorization')
            is_authorised = AuthenticationController().has_permission(request, view_permission)

            if authorization and is_authorised:
                return view(context, request)
            else:
                raise exc.HTTPForbidden()
        return wrapper_view
    else:
        return view
