from .base import *

DEBUG = False
SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysqltutorial',
        'USER' : 'root',
        'PASSWORD': config('DEPLOY_DATABSE_PASSWORD'),
        'PORT' : 3306,
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'charset': 'utf8mb4',  # 데이터베이스 한글도 저장하게 하게하기
        }
    }
}
