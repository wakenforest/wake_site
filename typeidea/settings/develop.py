from .base import * # NOQA
import pymysql

pymysql.install_as_MySQLdb()

DEBUG = True
# DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wakenforest_blog_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST':'127.0.0.1',
        'PORT':3306,
    },
    'mongotest':{
        'ENGINE' : None,
    }
}

import mongoengine
# 连接mongodb中数据库名称为mongotest5的数据库 iflashbuy_log
# mongoengine.connect("iflashbuy_log",host="127.0.0.1",port=27017)
mongoengine.connect("test_log",host="127.0.0.1",port=27017)

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

# INTERNAL_IPS = ['127.0.0.1']


REDIS_URL = 'redis://127.0.0.1:6379'

CACHES = {
    'default':{
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD': '<对应密码>',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
