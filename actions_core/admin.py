from django.contrib import admin

from .models import Organization, User, TimelineEntity, Event


admin.site.register((Organization, User, TimelineEntity, Event))
