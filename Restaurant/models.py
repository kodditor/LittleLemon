from django.db import models

# Create your models here.

class booking(models.Model):
    id = models.IntegerField(primary_key=True,)
    name = models.TextField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

class menu (models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'