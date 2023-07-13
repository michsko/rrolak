from django import forms 
from django.forms import ModelForm
from .models import Tanecnik
from .models import Tanecni_jednotka
from .models import Zavod 
from .models import Prihlaska_zavod

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
	
	




