from django import forms 
from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import Tanecnik
from .models import Tanecni_jednotka
from .models import Zavod 
from .models import Prihlaska_zavod
from .models import Tanecni_jednotka


#Create a forms here


class TanecnikForm(ModelForm):
	class Meta:
		model = Tanecnik
		fields =('klub', 'foto_tanecnik', 'jmeno', 'prijmeni', 'datum_narozeni', 'rodne_cislo', 
	'email', 'adresa', 'telefon', 'zdravotni_prohlidka', 'zdravotni_prohlidka_potvr', 
	'pas', 'doping', 'registr_csar', 'registr_zavodni_csar', 'registr_wrrc', 'tanecnik', 'trener', 'porotce', 'odborny_dozor')

		labels = {'klub':'Klub', 
		'foto_tanecnik': 'Foto tanecníka',
		'jmeno': '', 
		'prijmeni': '', 
		'datum_narozeni': '', 
		'rodne_cislo': '', 
		'email': '', 
		'adresa': '', 
		'telefon': '', 
		'zdravotni_prohlidka': '', 
		'zdravotni_prohlidka_potvr': 'Zdravotní prohlídka potvrzení',
		'pas': 'Kopie pasu', 
		'doping': 'Doping',
		

		}

		widgets = {'klub': forms.Select(attrs={'class': 'form-control'}), 
		'jmeno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno:',}), 
		'prijmeni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Příjmení:',}), 
		'datum_narozeni': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum narození: (RRRR-MM-DD)',}), 
		'rodne_cislo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rodné číslo:',}), 
		'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email:',}), 
		'adresa': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Adresa:',}), 
		'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Telefonní číslo:'}), 
		'zdravotni_prohlidka': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Zdravotní prohlídka DO: (RRRR-MM-DD)',}), 
		'registr_csar': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}), 
		'registr_zavodni_csar': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'registr_wrrc': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'tanecnik': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}), 
		'trener': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'porotce': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'odborny_dozor': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'})
		}
	
	


class TanecniJednotkaForm(ModelForm):
	class Meta(object):
		"""docstring fos Meta"""
		model = Tanecni_jednotka
		fields = ('klub', 'kategorie','jmeno_tanecni_jednotky','tanecnici')

		labels={}
		
		widgets={'klub': forms.Select(attrs={'class': 'form-control'}),
		'kategorie': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecni_jednotky': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno taneční jednotky'}),
		'tanecnici': forms.Select(attrs={'class': 'form-control'}),
		}
