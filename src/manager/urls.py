from django.urls import path

from . import views
from .utils import utils
from django.urls import reverse


urlpatterns = [
    path('', views.manager, name='manager-home'),
    path('approved/', views.approved, name='manager-approved'),
    path('print/', utils.print_pdf, name='manager-print'),
    path('update/<int:pk>', views.StayUpdate.as_view(), name='manager-update' ),
    path('update/<int:pk>/delete', views.StayDeleteView.as_view(), name='manager-delete' ),
]


#href="{% url 'manager-update' item.id %}"