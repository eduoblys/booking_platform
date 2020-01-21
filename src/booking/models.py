from django.db import models

class SimpleModel(models.Model):
    col = models.CharField(max_length=100)