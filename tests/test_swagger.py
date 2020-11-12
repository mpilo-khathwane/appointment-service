import os
from unittest import mock

from appointment_service.modules.pyramid_includes import swagger_yaml_to_json


def test_swagger_yaml_to_json():
    # Mock all required values
    config = mock.MagicMock()
    config.registry.settings = {'pyramid_swagger.schema_directory': 'appointment_service/api_docs',
                                'pyramid_swagger.yaml_file': 'swagger.yaml',
                                'pyramid_swagger.schema_file': 'swagger.json'}
    # Yaml to Json
    swagger_yaml_to_json(config)
    # Assert Json got created
    json_path = os.path.join(
        config.registry.settings['pyramid_swagger.schema_directory'],
        config.registry.settings['pyramid_swagger.schema_file'])
    assert os.path.isfile(json_path)
