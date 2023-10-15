from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.img = 'destination_1.jpg'
    dest1.name = 'Dhaka'
    dest1.desc = "The heart of Bangladesh"
    dest1.price = 800
    dest1.offer = True

    dest2 = Destination()
    dest2.img = 'destination_2.jpg'
    dest2.name = 'Chittagong'
    dest2.desc = 'The mother city of Ocean'
    dest2.price = '700'
    dest2.offer = True

    dest3 = Destination()
    dest3.img = 'destination_3.jpg'
    dest3.name = 'Kushtia'
    dest3.desc = 'The city of tradition'
    dest3.price = '600'
    dest3.offer = False

    dest4 = Destination()
    dest4.img = 'destination_4.jpg'
    dest4.name = 'Khulna'
    dest4.desc = 'City Beside Rupsha'
    dest4.price = '650'
    dest4.offer = False

    dest5 = Destination()
    dest5.img = 'destination_5.jpg'
    dest5.name = 'Rajshahi'
    dest5.desc = 'City of Mango'
    dest5.price = '650'
    dest5.offer = False


    dest6 = Destination()
    dest6.img = 'destination_6.jpg'
    dest6.name = 'Sylhet'
    dest6.desc = 'City of Hills, waterfalls'
    dest6.price = '700'
    dest6.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    return render(request, 'index.html', {'dests' : dests})