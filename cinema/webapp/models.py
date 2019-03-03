from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    release_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=50)


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row_number = models.IntegerField(max_length=3)
    seat_number = models.IntegerField(max_length=3)


class Show(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(decimal_places=2)
