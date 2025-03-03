from rest_framework import serializers
from .models import Movie


class MovieSeriaLizer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'

