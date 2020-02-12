from django.urls import path

from . import views

urlpatterns = [
    path('', views.manager, name='manager-home'),
    path('print/', views.print_pdf, name='manager-print'),
    path('update/<int:pk>', views.StayUpdate.as_view(), name='manager-update' )
]


#href="{% url 'manager-update' item.id %}"