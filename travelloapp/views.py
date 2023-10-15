from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Dhaka'
    dest1.desc = "The heart of Bangladesh"
    dest1.price = 800

    return render(request, 'index.html', {'dest1' : dest1})