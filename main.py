# See https://github.com/Azure/azure-sdk-for-python/issues/42337

from azure.monitor.opentelemetry import configure_azure_monitor

import logging
# logging.basicConfig(level=logging.DEBUG)

# Configure OpenTelemetry to use Azure Monitor with the
# APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.
configure_azure_monitor(
    logger_name=__name__
)
