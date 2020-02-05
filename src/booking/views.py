from django.shortcuts import render
from django.http import HttpResponse

from .forms import ReservationsForm

def home(request):
    return render(request, 'booking/home.html')



def showform(request):
    form = ReservationsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
        
    return render(request, 'booking/reservation.html', context)
