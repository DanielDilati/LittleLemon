from django.db import models

# Create your models here.

class MenuItems(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return(f'{self.title} : {self.price}')




class Booking(models.Model):
    name = models.CharField(max_length=225)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()