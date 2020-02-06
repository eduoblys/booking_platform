from django.db import models
from django.utils.translation import ugettext_lazy as _


class Reservations(models.Model):

    CHOICES = [
        ('1', _("one")),
        ('2', _("two")),
        ('3', _("three")),
        ('4', _("four")),
        ('5', _("five")),
        ('6', _("six")),
    ]


    firstname= models.CharField(verbose_name=_("first name*"), max_length=100, null=True)
    lastname= models.CharField(verbose_name=_("last name*"), max_length=100, null=True)
    email= models.EmailField(verbose_name=_("e-mail:"), blank=True, null=True)
    num_of_ppl = models.CharField(max_length=6, choices=CHOICES, null=True)
    comment= models.CharField(verbose_name=_("comment*"), max_length=10000, null=True)
    date_applied = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment



