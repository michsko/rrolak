from django.shortcuts import render
from . models import Tanecnik

# Create your views here.


def home(request):


	return render(request, 'web_app/home.html', {})




def tanecnik(request):

	tanecnik = Tanecnik.objects.all()
	
	return render(request, "web_app/tanecnik.html", {'tanecnik' : tanecnik,})

