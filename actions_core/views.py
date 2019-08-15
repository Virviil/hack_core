from django.shortcuts import get_object_or_404
from django.http.response import Http404, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser

from .models import User, TimelineEntity, Event
from .actions import init_integration_basket, init_bank_suggestion
from .serializers import TimelineEntitySerializer, EventSerializer


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

    # init integration basket
    init_integration_basket(user)
    init_bank_suggestion(user)

    return Response('user created!', status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_entities(request: Request):
    user_id = request.query_params.get('user_id')
    user = get_object_or_404(User, id=user_id)
    if isinstance(user, Http404):
        return Response('User not found!', status=status.HTTP_404_NOT_FOUND)

    suggestions = user.timeline_entities.filter(entity_type='s')
    suggestions_serializer = TimelineEntitySerializer(suggestions, many=True)

    rights = user.timeline_entities.filter(entity_type='r')
    rights_serializer = TimelineEntitySerializer(rights, many=True)

    response = {
        'rights': rights_serializer.data,
        'suggestions': suggestions_serializer.data
    }

    return JsonResponse(response, safe=False)


@api_view(['GET'])
def get_events(request: Request):
    user_id = request.query_params.get('user_id')
    user = get_object_or_404(User, id=user_id)
    if isinstance(user, Http404):
        return Response('User not found!', status=status.HTTP_404_NOT_FOUND)

    events = user.events.all().order_by('date')
    events_serializer = EventSerializer(events, many=True)

    return JsonResponse(events_serializer.data, safe=False)

