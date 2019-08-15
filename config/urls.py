from django.contrib import admin
from django.urls import path, include

from actions import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actions/', include(urls.urlpatterns))
]
