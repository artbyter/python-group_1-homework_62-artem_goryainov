from django.shortcuts import render

# Create your views here.

from webapp.models import Movie, Category, Hall, Seat, Show, Discount, Ticket,Reservation
from rest_framework import viewsets
from api_v1.serializers import MovieSerializer, CategorySerializer, HallSerializer, SeatSerializer, ShowSerializer, \
    DiscountSerializer, TicketSerializer, ReservationSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-release_date')
    serializer_class = MovieSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all().order_by('name')
    serializer_class = HallSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by('hall', 'row_number', 'seat_number')
    serializer_class = SeatSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all().order_by('start_time')
    serializer_class = ShowSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
