import os
import logging

import appointment_service.modules.pyramid_renderers as renderer_factory

from pyramid.config import Configurator
from appointment_service.clients import Clients
from appointment_service.configuration import Config
from appointment_service.authorization_view_deriver import authorization_view


def serve(global_config, **settings):
    config = Configurator(settings=settings)

    config.add_view_deriver(authorization_view)
    config.include('.cors')
    config.add_cors_preflight_handler()

    logging.info('Initialising configuration...')
    Config().configure()

    logging.info('Initialising clients...')
    Clients().configure()

    # Scan the current Python Package for any @configuration_decorators
    config.scan()

    logging.info('WSGI App being returned...')

    return config.make_wsgi_app()
