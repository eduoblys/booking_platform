from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
from .forms import ReservationsForm

def home(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    return render(request, 'booking/home.html')



def showform(request):
    form = ReservationsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
        
    return render(request, 'booking/reservation.html', context)
