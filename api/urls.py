from django.urls import path
from .views import HelloAPI, signUp, logIn, UserInfo,saveImage


urlpatterns = [
    path('hello/', HelloAPI),
    path('signup/', signUp),
    path('login/', logIn),
    path('info/', UserInfo),
    path('save/image/', saveImage),
]

