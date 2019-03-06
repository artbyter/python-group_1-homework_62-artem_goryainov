from django.db import models
import uuid
from datetime import datetime

CANCELED = 'CA'
REDEEMED = 'RE'
CREATED = 'CR'

RESERVATION_STATUS = (
    (CANCELED, 'Canceled'),
    (REDEEMED, 'Redeemed'),
    (CREATED, 'Created'),
)


# Create your models here.

class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    release_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='categories', blank=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return self.name


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
    row_number = models.IntegerField()
    seat_number = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return '{} row, {} seat in {}'.format(self.row_number, self.seat_number, self.hall)


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return '{} in {} on {}'.format(self.movie, self.hall, self.start_time.strftime('%d-%b-%y, %I:%M'))


class Discount(models.Model):
    name = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    start_time = models.DateTimeField(default=None, null=True, blank=True)
    end_time = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return '{}  {}%'.format(self.name, self.discount)


class Ticket(models.Model):
    show = models.ForeignKey(Show, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    discount = models.ForeignKey(Discount, models.PROTECT)

    def __str__(self):
        return '{} seat for {}'.format(self.seat, self.show)


def generate_id():
    return str(datetime.now().timestamp()).replace('.', '')


class Reservation(models.Model):
    uid = models.CharField(max_length=20, default=generate_id)
    show = models.ForeignKey(Show, on_delete=models.PROTECT)
    seat = models.ManyToManyField(Seat, blank=True)
    status = models.CharField(max_length=2, choices=RESERVATION_STATUS, default=CREATED)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'reservation №{}   on {}'.format(self.uid, self.show)
