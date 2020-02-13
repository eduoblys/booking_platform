from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Reservations


class ReservationForm(forms.ModelForm):
    class Meta:
        model= Reservations
        fields= ["firstname", "lastname", "email", "num_of_ppl", "comment", "start_date", "end_date"]
        widgets = {
            'start_date':DatePickerInput().start_of('event days'),
            'end_date':DatePickerInput().end_of('event days'),
        }