from rest_framework.serializers import ModelSerializer

from .models import TimelineEntity, Organization, Event


class ShortTimelineEntitySerializer(ModelSerializer):
    class Meta:
        model = TimelineEntity
        fields = ['id', 'name', 'description', 'end_date']


class ShortEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date']


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class FullTimelineEntitySerializer(ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = TimelineEntity
        fields = '__all__'


class FullEventSerializer(ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'



