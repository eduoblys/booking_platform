from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):
    class Meta:
        model= Reservations
        fields= ["firstname", "lastname", "email", "num_of_ppl", "comment"]