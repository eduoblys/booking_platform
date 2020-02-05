from django.db import models
from django.utils.translation import gettext as _


class Reservations(models.Model):
    firstname= models.CharField(verbose_name=_("first name*"), max_length=100)
    lastname= models.CharField(verbose_name=_("last name*"), max_length=100)
    email= models.EmailField(verbose_name=_("e-mail:"), blank=True)
    comment= models.CharField(verbose_name=_("comment*"), max_length=10000)

    def __str__(self):
        return self.comment
