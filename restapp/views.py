from django.contrib.auth.models import User
from django.core import serializers
from django.http import Http404
from rest_example.wsgi import ReturnAllDict
from restapp.ExcelSheet import *
from restapp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

import xlrd
AllList=[]
ApiHomeDict={}
InputDict={}
SuccessDict={}
FailureDict={}
JsonDict={}
e = ReturnAllDict()
AllList = e.returnDict()
ApiHomeDict=AllList[0]
InputDict=AllList[1]
SuccessDict=AllList[2]
FailureDict=AllList[3]
JsonDict=AllList[4]



class UserList(APIView):

    def get(self, request, format=None):
        print "ApiHomeDict all list ",ApiHomeDict
        print "InputDict all list ",InputDict
        print "SuccessDict all list ",SuccessDict
        print "FailureDict all list ",FailureDict
        print "JsonDict all list ",JsonDict
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        print "ApiHomeDict one list ",ApiHomeDict
        print "InputDict one list ", InputDict
        print "SuccessDict one list ", SuccessDict
        print "FailureDict one list ", FailureDict
        print "JsonDict one one ", JsonDict

        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk, format=None):
        user = User.objects.get(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
