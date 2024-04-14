import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info("Function startup")


def handler(event, _):
    logger.debug("[handler] %s", event)
    return
