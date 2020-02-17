from django.db import models
from django.utils.translation import ugettext_lazy as _

class Reservations(models.Model):

    CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
    ]

    firstname= models.CharField(verbose_name=_("first name"), max_length=100)
    lastname= models.CharField(verbose_name=_("last name"), max_length=100)
    email= models.EmailField(verbose_name=_("e-mail:"), blank=True, null=True)
    num_of_ppl = models.CharField(verbose_name=_("amount"), max_length=6, choices=CHOICES)
    comment= models.CharField(verbose_name=_("comment"), max_length=10000)
    start_date = models.DateField(verbose_name="date in",blank=True, null=True)
    end_date = models.DateField(verbose_name="date out",blank=True, null=True)
    date_applied = models.DateTimeField(verbose_name=_("date of application"),auto_now_add=True, null=True)
    stay_approved = models.BooleanField(verbose_name=_("approved"),null=True, default=False)
    
    def __str__(self):
        return self.firstname



