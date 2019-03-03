from webapp.models import Movie, Category, Hall, Seat, Show
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'poster', 'release_date', 'finish_date')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class HallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hall
        fields = ('id', 'name')

class SeatSerializer(serializers.HyperlinkedModelSerializer):
    hall=serializers.StringRelatedField()
    class Meta:
        model = Seat
        fields = ('id', 'hall','row_number','seat_number')

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    movie=serializers.StringRelatedField()
    hall=serializers.StringRelatedField()
    class Meta:
        model = Show
        fields = ('id', 'movie','hall','start_time','end_time','price')

