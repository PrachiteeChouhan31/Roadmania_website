from django.shortcuts import render
from .models import Destination,Entry,Tips,Image_Entry

def index(request):
    destinations=Destination.objects.order_by('date_added')
    context={'destinations':destinations}
    return render(request,'travels/index.html',context)

def destinations(request):
    """shows all the destinations place"""
    destinations=Destination.objects.order_by('date_added')
    context={'destinations':destinations}
    return render(request,'travels/destinations.html',context)

def destination(request, destination_id):
    """shows the description about the single destination"""
    destination=Destination.objects.get(id=destination_id)
    entries=destination.entry_set.get(id=destination_id)
    images=entries.image_entry_set.all()
    context={'destination':destination,'entries':entries,'images':images}
    return render(request, 'travels/destination.html',context)

def tips(request):
    """shows all the tips"""
    tips=Tips.objects.all()
    context={'tips':tips}
    return render(request,'travels/tips.html',context)