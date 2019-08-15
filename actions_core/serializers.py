from rest_framework.serializers import ModelSerializer

from .models import TimelineEntity, Organization, Event


class TimelineEntitySerializer(ModelSerializer):
    class Meta:
        model = TimelineEntity
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
