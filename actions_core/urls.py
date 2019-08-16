from django.urls import path

from .views import init_wizard, driving_license_wizard, get_entities, get_events, \
    get_entity_detail, get_event_detail


urlpatterns = [
    path('actions/init', init_wizard),
    path('actions/driving_license', driving_license_wizard),
    path('entities/', get_entities),
    path('events/', get_events),
    path('entities/<int:entity_id>', get_entity_detail),
    path('events/<int:entity_id>', get_event_detail)
]
