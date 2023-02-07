"""defines URLs for travels app"""
from django.urls import path
from . import views
app_name='travels'
urlpatterns=[
    #homepage
    path('', views.index, name='index'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:destination_id>', views.destination, name='destination'),
    path('tips/', views.tips, name='tips'),
    

]