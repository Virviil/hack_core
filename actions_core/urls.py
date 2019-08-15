from django.urls import path

from .views import init_wizard


urlpatterns = [
    path('init', init_wizard)
]
