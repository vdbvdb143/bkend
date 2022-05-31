from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User

from user.serializer import UserSerializer

class addUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def create(self,request):
        x=request.data
        print(x)
        temp=User.objects.get(username=x['username']) or User.objects.get(email=x['email'])
        if not temp:
            user = User.objects.create_user(x['username'],x['email'] ,x['password'])
            user.first_name = x['firstname']
            user.last_name = x['lastname']
            user.save()
            return Response({'status': True, 'message': 'Registered'})
        else:
            return Response({'status': False, 'message': 'Account already exist'})

class check(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def create(self,request):
        x=request.data
        temp=User.objects.get(username=x['username'])
        if temp:
            return Response({'status': True, 'message': 'Acess'})
        else:
            return Response({'status': False, 'message': 'User doesnot exist'})