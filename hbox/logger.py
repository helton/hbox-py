import logging

from hbox.config import load_config


class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno != logging.INFO:
            self._style._fmt = "[%(levelname)s] %(message)s"
        else:
            self._style._fmt = "%(message)s"
        return super().format(record)


def get_logger(name: str):
    logger = logging.getLogger(name)
    cfg = load_config()
    logger.setLevel(logging.DEBUG if cfg.debug else logging.INFO)
    formatter = CustomFormatter()
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
