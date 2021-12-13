from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Ps5_games


class Ps5_gamesSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'author', 'updated', 'timestamp', 'content','published']
        model = Ps5_games