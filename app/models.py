from django.db import models
from django.contrib.auth.models import User

class JsonDocument(models.Model):
    data = models.JSONField()


class JsonTemplate(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class JsonField(models.Model):
    DATA_TYPES = [
        ('str', 'String'),
        ('int', 'Integer'),
        ('bool', 'Boolean'),
        ('float', 'Float'),
    ]
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=10, choices=DATA_TYPES)
    template = models.ForeignKey(JsonTemplate, on_delete=models.CASCADE)
    min_value = models.FloatField(null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)
    choices = models.JSONField(null=True, blank=True)
    min_length = models.IntegerField(null=True, blank=True)
    max_length = models.IntegerField(null=True, blank=True)
