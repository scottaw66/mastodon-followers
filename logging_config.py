log_settings = {
    'version': 1,
    'disable-existing-loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%m/%d/%Y %I:%M:%S %p'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': 'followers.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 10
        }
    },
    'loggers': {
        'main': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}