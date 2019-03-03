from django.shortcuts import render

# Create your views here.

from webapp.models import Movie
from rest_framework import viewsets
from api_v1.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-release_date')
    serializer_class = MovieSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()