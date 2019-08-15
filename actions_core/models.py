from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOISES = (
    ('m', 'Male'),
    ('f', 'Female')
)
MARITAL_CHOISES = (
    ('s', 'Single'),
    ('m', 'Married')
)
TIMELINE_ENTITY_TYPES = (
    ('Right', 'r'),
    ('Suggestion', 's')
)


class User(models.Model):
    aliah_date = models.DateField()
    gender = models.CharField(choices=GENDER_CHOISES, max_length=1)
    age = models.IntegerField()
    marital_status = models.CharField(choices=MARITAL_CHOISES, max_length=1)
    number_of_children = models.IntegerField()

    objects = models.Manager


class Organization(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    url = models.URLField()
    logo_url = models.URLField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)

    objects = models.Manager

    def __str__(self):
        return self.name


class TimelineEntity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    entity_type = models.CharField(choices=TIMELINE_ENTITY_TYPES, max_length=10)
    start_date = models.DateField()
    end_date = models.DateField(null=True)  # todo think about suggestions
    is_complited = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)

    objects = models.Manager

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    date = models.DateField()

    objects = models.Manager



