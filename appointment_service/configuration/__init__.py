import os
import logging
import threading

from mongoengine import connect
from appointment_service.configuration.__service_config import ServiceConfig

logger = logging.getLogger(__name__)


class Config(object):

    service_config = None

    _instance = None
    _lock = threading.Lock()
    _db_client = None

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Config, cls).__new__(cls)
                    cls._instance.logger = logging.getLogger(__name__)
        return cls._instance

    def configure(self):
        with self.__class__._lock:
            self._instance._configure_service_config()

    def _connect_db(self):
        host = self._instance.service_config.get_str("mongo_db.host")
        port = self._instance.service_config.get_int("mongo_db.port")
        db = self._instance.service_config.get_str("mongo_db.db")

        self._instance.logger.info(f"Initialising db connection on host: {host}, port: {port}, db: {db}")
        connect(db=db, host=host, port=port)

    def _configure_service_config(self):
        file_name = os.environ.get("CONFIG_FILE_NAME")  # todo: might need to add ENV VARS
        if not file_name:
            file_name = "development.ini"
        ini_file = f"appointment_service/configuration/{file_name}"

        self._instance.logger.info(f"Initialising config file = {ini_file}")

        # Initialise service_config
        self._instance.service_config = ServiceConfig(ini_files=[ini_file])
