from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ListCreateTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = "__all__"
        extra_kwargs = {'uploaded_at': {'read_only': True}}
