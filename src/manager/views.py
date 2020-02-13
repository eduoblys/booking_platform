from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView


from booking.models import  Reservations

@login_required
def manager(request):
      
    data = Reservations.objects.all()
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj,
        'data': data
    }
    return render(request, "manager/manager.html", context)


class StayUpdate(LoginRequiredMixin, UpdateView):
    model = Reservations
    fields = ['firstname', 'lastname', 'email', 'num_of_ppl','comment', 'stay_approved']
    template_name_suffix = '_update_form'
    success_url='/manager'

    def form_valid(self, form):
        messages.success(self.request, 'update succesful')
        return super().form_valid(form)
        
        
class StayDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservations
    success_url = '/manager'

    