from rest_framework import serializers
from .modules import Moviedata
from .serializations import MovieSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating']

