from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponseNotAllowed

from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser

from .models import User


@api_view(['POST'])
@parser_classes([JSONParser])
def init_wizard(request: Request):
    raw_user_data = request.data
    user = User.objects.create(
        aliah_date=raw_user_data['aliah_date'],
        gender=raw_user_data['gender'],
        age=raw_user_data['age'],
        marital_status=raw_user_data['marital_status'],
        number_of_children=raw_user_data['number_of_children']
    )
    user.save()
    return Response('user created!', status=status.HTTP_201_CREATED)



