from django.shortcuts import render

from booking.models import Reservations

def manager(request):
      
    data = Reservations.objects.all()
    context={
      'data': data
    }
    return render(request, "manager/manager.html", context)