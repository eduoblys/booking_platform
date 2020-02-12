from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from booking.models import  Reservations




@login_required
def manager(request):
      
    data = Reservations.objects.all()


    context={
        'data': data

    }
    return render(request, "manager/manager.html", context)


class StayUpdate(LoginRequiredMixin, UpdateView):
    model = Reservations
    fields = ['firstname', 'lastname', 'email', 'num_of_ppl','comment', 'stay_approved']
    template_name_suffix = '_update_form'

    
    def form_valid(self, form):
        messages.success(self.request, 'update succesful')
          
        return redirect('manager-home')




def print_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')