from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager, name='manager-home'),
    path('print/', views.print_pdf, name='manager-print'),

]
