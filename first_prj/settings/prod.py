from .base import *

DEBUG = False
SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysqltutorial',
        'USER': 'codestates',
        'PASSWORD': config('DEPLOY_DATABSE_PASSWORD'),
        'PORT': 3306,
        'HOST': 'database-1.c9ohwqemljbd.ap-northeast-2.rds.amazonaws.com',
        'OPTIONS': {
            'charset': 'utf8mb4',  # 데이터베이스 한글도 저장하게 하게하기
        }
    }
}
