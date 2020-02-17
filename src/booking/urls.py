
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='booking-home'),
    path('reservation/', views.showform, name='reservation-form'),

]
