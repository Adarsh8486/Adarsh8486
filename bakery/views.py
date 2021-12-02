
from http.client import responses
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registerUser, Ingredients
from rest_framework import  status
from .serializer import registerUserSerializers,  IngredientsSerializers, registeruserSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def userDetail(request, pk):

    user = registerUser.objects.get(id = pk)

    ser = registeruserSerializers(user)
    json_data= JSONRenderer().render(ser.data)

    return HttpResponse(json_data, content_type = "application/json")


def userDetails(request):

    user = registerUser.objects.all()

    ser = registeruserSerializers(user,many = True)
    json_data= JSONRenderer().render(ser.data)

    return HttpResponse(json_data, content_type = "application/json")


class RegisterAPIView(APIView):

    serializer_class = registerUserSerializers

    def post(self, request, format=None):
        ser = self.serializer_class(data= request.data)
        if ser.is_valid():
            user= ser.save()

            refresh = RefreshToken.for_user(user)
            
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


def productDetails(request):

    user = Ingredients.objects.all()

    ser =  IngredientsSerializers(user,many = True)
    json_data= JSONRenderer().render(ser.data)

    return HttpResponse(json_data, content_type = "application/json")

def productDetail(request, pk):

    user = Ingredients.objects.get(id = pk)

    ser = IngredientsSerializers(user)
    json_data= JSONRenderer().render(ser.data)

    return HttpResponse(json_data, content_type = "application/json")




