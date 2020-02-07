from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import translation
from .forms import ReservationForm

def home(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    return render(request, 'booking/home.html')



def showform(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('firstname')
            messages.success(request, 'Reservation succesful')
            return redirect('booking-home')
    else:
        form = ReservationForm()
    return render(request, 'booking/reservation.html', {'form': form})
