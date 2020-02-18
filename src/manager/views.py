from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.translation import ugettext as _


from django.urls import reverse

from . import views
from booking.models import  Reservations
from .models import Tennants


@login_required
def manager(request):
      
    data = Reservations.objects.all()
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj,
        'data': data,
    }
    return render(request, "manager/manager.html", context)


@login_required
def approved(request):    
    data = Reservations.objects.filter(stay_approved="True")
    context={
        'data': data,
    }
    return render(request, "manager/approved.html", context)


class StayUpdate(LoginRequiredMixin, UpdateView):
    model = Reservations
    fields = ['firstname', 'lastname', 'email', 'num_of_ppl','comment', 'stay_approved']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('manager-home')

    def form_valid(self, form):
        messages.success(self.request, _('update succesful'))
        return super().form_valid(form)
        
        
class StayDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservations
    
    def get_success_url(self):
            return reverse('manager-home')

    