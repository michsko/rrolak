from django.shortcuts import render
from . models import Tanecnik

# Create your views here.


def home(request):


	return render(request, 'web_app/home.html', {})



def tanecnici(request):

	tanecnici_klub = Tanecnik.objects.all()
	
	return render(request, "web_app/tanecnici.html", {'tanecnici_klub' : tanecnici_klub,})


def tanecnik(request, pk):

	tanecnik = Tanecnik.objects.get(id=pk)
	
	return render(request, "web_app/tanecnik.html", {'tanecnik' : tanecnik,})


def tanecnici_prehled(request):

	tanecnici_prehled = Tanecnik.objects.all()

	return render (request, "web_app/tanecnici_prehled.html", {'tanecnici_prehled': tanecnici_prehled, })
