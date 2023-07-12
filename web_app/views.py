from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Tanecnik
from .models import Zavod
from .models import Prihlaska_zavod
from .models import Tanecni_jednotka
from .models import Profil
from .forms import TanecnikForm
from .forms import TanecniJednotkaForm 

# Create your views here.


def home(request):


	return render(request, 'web_app/home.html', {})

# kluby

def kluby_prehled(request):
	kluby_prehled = Profil.objects.all()

	return render(request, "web_app/kluby_prehled.html", {'kluby_prehled': kluby_prehled,})



#tanecnici 

def tanecnici(request):

	tanecnici_klub = Tanecnik.objects.all()
	
	return render(request, "web_app/tanecnici.html", {'tanecnici_klub' : tanecnici_klub,})


def tanecnik(request, pk):

	tanecnik = Tanecnik.objects.get(id=pk)
	
	return render(request, "web_app/tanecnik.html", {'tanecnik' : tanecnik,})


def tanecnici_prehled(request):

	tanecnici_prehled = Tanecnik.objects.all()

	return render(request, "web_app/tanecnici_prehled.html", {'tanecnici_prehled': tanecnici_prehled, })


def pridat_tanecnika(request):
	submitted = False

	if request.method == "POST":
		form = TanecnikForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,("Tanečník byl úspěšně přidán."))
			return redirect("tanecnici_prehled")
	else: 
		form = TanecnikForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, "web_app/pridat_tanecnika.html", {'form': form, 'submitted': submitted, })


def smazat_tanecnika(request, pk):

	tanecnik = Tanecnik.objects.get(id=pk)
	tanecnik.delete()
	messages.success(request, ('Tanečník byl smazán.'))
	return redirect('tanecnici_prehled')


def upravit_tanecnika(request, pk):

	tanecnik = Tanecnik.objects.get(id=pk)

	form = TanecnikForm(request.POST or request.FILES or None, instance=tanecnik)
	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o tanečníkovi byly změněny.'))
		return redirect('tanecnici_prehled')
	else:

		return render(request, "web_app/upravit_tanecnika.html", {'tanecnik': tanecnik, 'form': form,})


# tanecni jednotka 



def pridat_tj(request):
	submitted = False
	if request.method == "POST":
		form = TanecniJednotkaForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ("Taneční jednotka byla úspěšně přidána."))
			return redirect('tanecni_jednotky_prehled')

	else:
		form = TanecniJednotkaForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, "web_app/pridat_tj.html", {'form': form, 'submitted': submitted})


def smazat_tj(request, pk):

	tanecni_jednotka = Tanecni_jednotka.objects.get(id=pk)
	tanecni_jednotka.delete()
	messages.success(request, ("Taneční jednotka byla úspěšně smazána."))
	
	return redirect('Tanecni_jednotky_prehled')


def tanecni_jednotky_prehled(request):
	
	tanecni_jednotky = Tanecni_jednotka.objects.all()

	return render(request, "web_app/tanecni_jednotky_prehled.html", {'tanecni_jednotky': tanecni_jednotky})



def upravit_tj(request, pk):

	tanecni_jednotka = Tanecni_jednotka.objects.get(id=pk)

	form = TanecniJednotkaForm(request.POST or None, instance=tanecni_jednotka)
	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o Taneční jednotce byly změněny'))
		return redirect('tanecni_jednotky_prehled')
	else:
		return render(request, "web_app/upravit_tj.html", {'tanecni_jednotka': tanecni_jednotka, 'form': form})





# zavody

def zavody_prehled(request):

	zavody = Zavod.objects.all()
	prihlasky = Prihlaska_zavod.objects.all()
	tanecni_jednotky = Tanecni_jednotka.objects.all()

	return render(request, "web_app/zavody.html", {'zavody': zavody, 'prihlasky': prihlasky, 'tanecni_jednotky': tanecni_jednotky})



def prihlasky_prehled(request, pk):

	zavod = Zavod.objects.get(id=pk)

	prihlasky = Prihlaska_zavod.objects.filter(zavod_id = pk)
	

	return render(request, "web_app/prihlasky_prehled.html", {'prihlasky': prihlasky, 'zavod': zavod})




