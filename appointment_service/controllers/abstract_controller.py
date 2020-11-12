import abc

from appointment_service.clients import Clients
from appointment_service.configuration import Config


class AbstractController(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.clients = Clients()
        self.config = Config()
