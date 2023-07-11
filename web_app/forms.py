from django import forms 
from django.forms import ModelForm
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
	'pas', 'doping', 'registr_csar', 'registr_zavodni_csar', 'registr_wrrc')

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
		}
	
	


class TanecniJednotkaForm(ModelForm):
	class Meta(object):
		"""docstring fos Meta"""
		model = Tanecni_jednotka
		fields = ('klub', 'kategorie','jmeno_tanecni_jednotky','jmeno_tanecnik1', 
	    	'jmeno_tanecnik2', 'jmeno_tanecnik3', 'jmeno_tanecnik4', 
	    	'jmeno_tanecnik5', 'jmeno_tanecnik6', 'jmeno_tanecnik7',
	    	 'jmeno_tanecnik8', 'jmeno_tanecnik9', 'jmeno_tanecnik10',
	    	  'jmeno_tanecnik11', 'jmeno_tanecnik12', 'jmeno_tanecnik13',
	    	   'jmeno_tanecnik14', 'jmeno_tanecnik15', 'jmeno_tanecnik16')

		labels={}
		
		widgets={'klub': forms.Select(attrs={'class': 'form-control'}),
		'kategorie': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecni_jednotky': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno taneční jednotky'}),
		'jmeno_tanecnik1': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik2': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik3': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik4': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik5': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik6': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik7': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik8': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik9': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik10': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik11': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik12': forms.Select(attrs={'class': 'form-control'}),		
		'jmeno_tanecnik13': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik14': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik15': forms.Select(attrs={'class': 'form-control'}),
		'jmeno_tanecnik16': forms.Select(attrs={'class': 'form-control'}),


		}