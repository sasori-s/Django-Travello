from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Dhaka'
    dest1.desc = "The heart of Bangladesh"
    dest1.price = 800

    dest2 = Destination()
    dest2.name = 'Chittagong'
    dest2.desc = 'The mother city of Ocean'
    dest2.price = '700'

    dest3 = Destination()
    dest3.name = 'Kushtia'
    dest3.desc = 'The city of tradition'
    dest3.price = '600'

    dest4 = Destination()
    dest4.name = 'Khulna'
    dest4.desc = 'City Beside Rupsha'
    dest4.price = '650'

    dest5 = Destination()
    dest5.name = 'Rajshahi'
    dest5.desc = 'City of Mango'
    dest5.price = '650'

    dest6 = Destination()
    dest6.name = 'Sylhet'
    dest6.desc = 'City of Hills, waterfalls'
    dest6.price = '700'

    return render(request, 'index.html', {'dest1' : dest1, 'dest2' : dest2, 'dest3': dest3, 'dest4': dest4, 'dest5': dest5, 'dest6': dest6})