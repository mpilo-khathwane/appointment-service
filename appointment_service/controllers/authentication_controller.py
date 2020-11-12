import json
import logging
import pyramid.httpexceptions as exc
from requests.exceptions import HTTPError

from appointment_service.models.models import *
from appointment_service.controllers.abstract_controller import AbstractController


class AuthenticationController(AbstractController):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def login(self, username, password):
        #todo call to client
        pass

    def logout():
        #todo call to client
        pass
