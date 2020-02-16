

#from ..bookingapp.widgets import BootstrapDateTimePickerInput
##DateInput(attrs={'class': 'datepicker'})

from django.forms import ModelForm, Textarea, DateInput

from .models import Reservations


class DateInput(DateInput):
    input_type = 'date'


class ReservationForm(ModelForm):
    class Meta:
        model= Reservations

        fields= ["firstname", "lastname", "email", "num_of_ppl", "comment", "start_date", "end_date"]
        widgets = {
            'comment' : Textarea(attrs={'rows': 7}),
            'start_date':DateInput(),
            'end_date':DateInput(),

        }    
    




"""
class ReservationForm(ModelForm):
    class Meta:
        model= Reservations

        fields= ["firstname", "lastname", "email", "num_of_ppl", "comment", "start_date", "end_date"]
        widgets = {
            'comment' : Textarea(attrs={'rows': 7}),
            'start_date':DatePickerInput().start_of('event days'),
            'end_date':DatePickerInput().end_of('event days'),

        }    
    
"""