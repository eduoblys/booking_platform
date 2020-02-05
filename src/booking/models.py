from django.db import models

class Reservations(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.EmailField()
    comment= models.TextField(max_length=10000)

    def __str__(self):
        return self.comment
