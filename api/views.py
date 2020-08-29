from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serialize import CreateUserSerializer
from polls.models import User


import json
import bcrypt
# pip install PyJWT
import jwt
from decouple import config


# False if not in os.environ


# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


@api_view(['POST'])
def signUp(request):
    email = request.data.get('email')
    password = request.data.get('password')
    hashingPassword = password.encode('utf-8')
    password_crypt = bcrypt.hashpw(hashingPassword, bcrypt.gensalt())
    password_crypt2 = password_crypt.decode('utf-8')
    try:
        one_user = User.objects.get(email=email)
        result = CreateUserSerializer(one_user)
    except User.DoesNotExist:
        data = User.objects.create(
            email=email, password=password_crypt2
        )
        result = CreateUserSerializer(data)
        print(result.data, '12312312')
        print('except')

    return JsonResponse({'success': True, 'id' : result.data['id']})


# login
@api_view(['POST'])
def logIn(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        oneUser = User.objects.get(email=email)
        user = CreateUserSerializer(oneUser)

        if bcrypt.checkpw(password.encode('utf-8'), user.data['password'].encode('utf-8')):
            token = jwt.encode({'email': user.data['email']}, config('JWT_SECRET'), algorithm="HS256")
            token = token.decode('utf-8')
            # jwt decoding(Decryption)
            # token = jwt.decode(token, 'SECRET_KEY', algorithm="HS256")
            return JsonResponse({'success': True, 'token': token, 'status': 200 })
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'status': 401})


@api_view(['GET'])
def UserInfo(request):
    # token 저장소 request.headers.Authorization
    print(config('a'))
    return Response('확인')




