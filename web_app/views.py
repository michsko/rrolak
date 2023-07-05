from django.shortcuts import render
from .models import Tanecnik
from .models import Zavod
from .models import Prihlaska_zavod
from .models import Tanecni_jednotka
from .models import Profil


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

	return render(request, "web_app/tanecnici_prehled.html", {'tanecnici_prehled': tanecnici_prehled, })




def zavody_prehled(request):

	zavody = Zavod.objects.all()
	prihlasky = Prihlaska_zavod.objects.all()
	tanecni_jednotky = Tanecni_jednotka.objects.all()

	return render(request, "web_app/zavody.html", {'zavody': zavody, 'prihlasky': prihlasky, 'tanecni_jednotky': tanecni_jednotky})



def prihlasky_prehled(request, pk):

	zavod = Zavod.objects.get(id=pk)

	prihlasky = Prihlaska_zavod.objects.filter(zavod_id = pk)
	

	return render(request, "web_app/prihlasky_prehled.html", {'prihlasky': prihlasky, 'zavod': zavod})



def tanecni_jednotky_prehled(request):

	tanecni_jednotky = Tanecni_jednotka.objects.all()

	return render(request, "web_app/", {'tanecni_jednotky': tanecni_jednotky})


