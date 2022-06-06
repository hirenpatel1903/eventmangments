import logging

logger = logging.getLogger("django")

class Logger:
    def __init__(self):
        pass

    @classmethod
    def logInfo(cls, msg):
        print("INFO | ", msg)
        logger.info(msg)

    @classmethod
    def logWarning(cls, msg):
        logger.warning(msg)

    @classmethod
    def logError(cls, msg):
        print("ERROR | ", msg)
        logger.error(msg)

    @classmethod
    def logDebug(cls, msg):
        logger.debug(msg)
