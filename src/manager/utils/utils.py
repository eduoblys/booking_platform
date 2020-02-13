
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from booking.models import Reservations



def print_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    data = Reservations.objects.all()
    b=0
    for e in data:
        p.drawString(60, 600-b,  "name:")
        p.drawString(100, 600-b,  str(e))
        b += 12
    

    msg = "string1"
    #p.drawString(100, 100, "Hello111 world!" + fnamed)
    p.drawString(100, 200, "Hello111 world!" + msg)



    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
#    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
    return FileResponse(buffer, filename='hello.pdf')