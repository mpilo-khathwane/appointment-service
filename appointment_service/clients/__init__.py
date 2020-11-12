import logging
import threading

from appointment_service.configuration import Config


class Clients(object):
    _config = None
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Clients, cls).__new__(cls)
                    cls._instance.logger = logging.getLogger(__name__)
        return cls._instance

    def configure(self):
        with self.__class__._lock:
            self._instance._config = Config()
