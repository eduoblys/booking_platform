from django.db import models

from booking.models import Reservations


class Tennants(models.Model):
    
    reservationsAccepted =  models.ManyToManyField(Reservations)

