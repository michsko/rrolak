from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
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



def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username=username, password=password)

		if user is not None: 
			auth.login(request, user)
			messages.success(request, ('Vaše přihlášení proběhlo úspěšně.'))
			return redirect ('klub')
		else: 
			messages.success(request, ("Nastal problém s vašim prihlašením."))
			return redirect('login')
	else:
		return render(request, "web_app/login.html", {})



def logout(request):
	auth.logout(request)
	messages.success(request, ('Byy jste odhlašeni.'))

	return redirect('login')



@login_required(login_url='login')
def klub(request):
	
	user_object = User.objects.get(username=request.user.username)
	klub_profile = Profil.objects.get(klub=user_object)
	tanecnici = Tanecnik.objects.all().filter(klub=user_object)
	tanecni_jednotky = Tanecni_jednotka.objects.all().filter(klub=user_object)

	return render(request, "web_app/klub.html", 
		{'klub_profile': klub_profile, 
		'tanecnici': tanecnici,
		'tanecni_jednotky': tanecni_jednotky})




#tanecnici 

@login_required(login_url="login")
def tanecnici(request):

	tanecnici_klub = Tanecnik.objects.all()
	
	return render(request, "web_app/tanecnici.html", {'tanecnici_klub' : tanecnici_klub,})



@login_required(login_url="login")
def tanecnik(request, pk):

	tanecnik = Tanecnik.objects.get(id=pk)
	
	return render(request, "web_app/tanecnik.html", {'tanecnik' : tanecnik,})



@login_required(login_url="login")
def tanecnici_prehled(request):

	tanecnici_prehled = Tanecnik.objects.all()

	return render(request, "web_app/tanecnici_prehled.html", {'tanecnici_prehled': tanecnici_prehled, })



@login_required(login_url="login")
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





@login_required(login_url="login")
def smazat_tanecnika(request, pk):

	tanecnik = Tanecnik.objects.get(id=pk)
	tanecnik.delete()
	messages.success(request, ('Tanečník byl smazán.'))
	return redirect('tanecnici_prehled')



@login_required(login_url="login")
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

@login_required(login_url="login")
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




@login_required(login_url="login")
def smazat_tj(request, pk):

	tanecni_jednotka = Tanecni_jednotka.objects.get(id=pk)
	tanecni_jednotka.delete()
	messages.success(request, ("Taneční jednotka byla úspěšně smazána."))
	
	return redirect('Tanecni_jednotky_prehled')




@login_required(login_url="login")
def tanecni_jednotky_prehled(request):
	
	tanecni_jednotky = Tanecni_jednotka.objects.all()

	return render(request, "web_app/tanecni_jednotky_prehled.html", {'tanecni_jednotky': tanecni_jednotky})





@login_required(login_url="login")
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
@login_required(login_url="login")
def zavody_prehled(request):

	zavody = Zavod.objects.all()
	prihlasky = Prihlaska_zavod.objects.all()
	tanecni_jednotky = Tanecni_jednotka.objects.all()

	return render(request, "web_app/zavody.html", {'zavody': zavody, 'prihlasky': prihlasky, 'tanecni_jednotky': tanecni_jednotky})




@login_required(login_url="login")
def prihlasky_prehled(request, pk):

	zavod = Zavod.objects.get(id=pk)

	prihlasky = Prihlaska_zavod.objects.filter(zavod_id = pk)
	

	return render(request, "web_app/prihlasky_prehled.html", {'prihlasky': prihlasky, 'zavod': zavod})




