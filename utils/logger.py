import logging


def get_logger(name: str, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    )

    # create a console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # set the formatters to the two handlers
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger
