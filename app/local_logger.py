import os

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "detailed": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s[%(asctime)s] %(cyan)s%(module)-0s.%(funcName)s() %(green)s %(lineno)d: %(white)s%(message)s",
            "datefmt": "%b %d %Y %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "app_log": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "{}/logs/app.log".format(
                os.path.dirname(os.path.realpath(__file__))
            ),
            "maxBytes": 50000,
            "formatter": "detailed",
        },
    },
    "loggers": {
        "app": {
            "handlers": [
                "app_log",
            ],
            "level": "DEBUG",
        },
    },
}
