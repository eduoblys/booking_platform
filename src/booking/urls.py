
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='booking-home'),
    path('reservation/', views.showform, name='reservation-form'),
    path('simple_url/', views.simple_view, name='form'),

]
