import os

LOGGING_ROOT = os.getenv('SERVICE_LOGS_DIR', '/tmp')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(levelname)s]: %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s(): %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'formatter': 'verbose',
            'class': 'logging.StreamHandler'
        },
        'ServiceFileHandler': {
            'formatter': 'verbose',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'app.log'),
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 5
        },
        'ErrorFileHandler': {
            'formatter': 'verbose',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'error.log'),
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 5
        }
    },
    'loggers': {
        'gunicorn.access': {
            'handlers': ['ServiceFileHandler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        }, 
        'gunicorn.error': {
            'handlers': ['ErrorFileHandler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'aiohttp.server': {
            'handlers': ['ErrorFileHandler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        '': {
            'handlers': ['ServiceFileHandler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
