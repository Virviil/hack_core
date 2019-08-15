from django.urls import path

from .views import init_wizard, get_entities, get_events


urlpatterns = [
    path('actions/init', init_wizard),
    path('entities/', get_entities),
    path('events/', get_events)
]
