
from azure.monitor.opentelemetry._configure import _setup_instrumentations, _get_configurations

import logging
logging.basicConfig(level=logging.DEBUG)

configurations = _get_configurations(logger_name=__name__)

_setup_instrumentations(
    configurations
)
