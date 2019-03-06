from webapp.models import Movie, Category, Hall, Seat, Show, Discount, Ticket, Reservation,RESERVATION_STATUS
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:category-detail')

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'description')


class InlineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    categories = InlineCategorySerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:movie-detail')

    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Category.objects.all(),
        source='categories'
    )

    class Meta:
        model = Movie
        fields = (
            'url', 'id', 'name', 'description', 'poster', 'categories', 'category_ids', 'release_date', 'finish_date')


class InlineSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('id', 'row_number', 'seat_number')


class SeatSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:seat-detail')
    hall_url = serializers.HyperlinkedRelatedField(view_name='api_v1:hall-detail', read_only=True, source='hall')


    class Meta:
        model = Seat
        fields = ('url', 'id', 'row_number', 'seat_number', 'hall', 'hall_url')


class HallSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:hall-detail')
    seats = InlineSeatSerializer(many=True, read_only=True)

    class Meta:
        model = Hall
        fields = ('url', 'id', 'name', 'description', 'seats')


class ShowSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:show-detail')
    movie_url = serializers.HyperlinkedRelatedField(view_name='api_v1:movie-detail', read_only=True, source='movie')
    hall_url = serializers.HyperlinkedRelatedField(view_name='api_v1:hall-detail', read_only=True, source='hall')

    class Meta:
        model = Show
        fields = ('url', 'id', 'movie', 'movie_url', 'hall', 'hall_url', 'start_time', 'end_time', 'price')


class DiscountSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:discount-detail')

    class Meta:
        model = Discount
        fields = ('url', 'id', 'name', 'discount', 'start_time', 'end_time')


class TicketSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:ticket-detail')
    show_url = serializers.HyperlinkedRelatedField(view_name='api_v1:show-detail', read_only=True, source='show')
    seat_url = serializers.HyperlinkedRelatedField(view_name='api_v1:seat-detail',  read_only=True, source='seat')
    discount_url = serializers.HyperlinkedRelatedField(view_name='api_v1:discount-detail', read_only=True,
                                                       source='discount')

    class Meta:
        model = Ticket
        fields = ('url', 'id', 'show', 'show_url', 'seat', 'seat_url', 'discount', 'discount_url')


class ReservationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:reservation-detail')
    show_url = serializers.HyperlinkedRelatedField(view_name='api_v1:show-detail', read_only=True, source='show')
    seat_url = serializers.HyperlinkedRelatedField(view_name='api_v1:seat-detail', many=True, read_only=True, source='seat')
    status = serializers.ChoiceField(choices=RESERVATION_STATUS)

    class Meta:
        model = Reservation
        fields = ('url', 'id', 'uid', 'show', 'show_url', 'seat', 'seat_url', 'status', 'create_date', 'update_date')