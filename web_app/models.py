from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from datetime import datetime


Klub = get_user_model()


# Create your models here.


class Profil(models.Model):
	klub = models.ForeignKey(Klub, on_delete=models.CASCADE)
	id_klub = models.IntegerField()
	logo_klub = models.ImageField(upload_to='klub_logo', default='csar_logo/logo_csar.jpeg')
	info = models.TextField(blank=True)
	adressa = models.CharField(max_length=255, blank=True)
	email = models.CharField(max_length=255, blank=True)
	telefon = models.CharField(max_length=255, blank=True)
	aktivni = models.BooleanField(default=True)

	def __str__ (self):
		return self.klub.username


class Tanecnik(models.Model):
	klub = models.ForeignKey(Klub, on_delete=models.CASCADE)
	foto_tanecnik = models.ImageField('Fotografie', upload_to='foto_tanecnik', default='foto_tanecnik/pic.jpg')
	jmeno = models.CharField('Jméno', max_length=255, blank=False)
	prijmeni = models.CharField('Příjmení',max_length=255, blank=False)
	datum_narozeni = models.DateField('Datum narození', blank=False)
	rodne_cislo = models.IntegerField('Rodné číslo', blank=False)
	email = models.EmailField('Email', blank=False)
	telefon = models.CharField('Telefonní číslo', max_length=255, blank=False)
	zdravotni_prohlidka = models.DateField('Zdravotní prohlídka DO: ', blank=False)
	zdravotni_prohlidka_potvr = models.FileField('Zdravotní prohlídka', upload_to='zdravotni_prohlidka', blank=True)
	pas = models.FileField('Kopie pasu', upload_to='kopie_pasu', blank=True)
	doping = models.FileField('Dopingove prohlašení', upload_to='dopingove_prohlaseni', blank=True)
	


	registr_csar = models.BooleanField('Registrace csar', default=False, null=True)
	datum_registrace = models.DateField(date.today(), null=True, blank=True)
	registrace_do = models.DateField(date.today().day+364, null=True, blank=True)
	
	
	registr_zavodni_csar = models.BooleanField('Zavodni registrace', default=False, null=True)
	datum_zavodni_registrace_csar = models.DateField(date.today(), null=True, blank=True)
	zavodni_registrace_do = models.DateField(date.today().day+364, null=True, blank=True)
	

	registr_wrrc = models.BooleanField('Registrace wrrc', default=False, null=True)
	datum_registrace_wrrc = models.DateField(date.today(), null=True, blank = True)
	registrace_wrrc_do = models.DateField(date.today().day+364, null=True, blank=True)
	
	

	def __str__(self):
		return self.jmeno + " " + self.prijmeni + " " + str(self.datum_narozeni) + " " + str(self.rodne_cislo)


	@property
	def Dny_do_nove_registrace_csar(self):
		dnes = date.today()
		if self.registrace_do <= dnes:
			stripped_dny = "Registrace ČSAR vypršela."
		else:
			dny_do_nove_registrace = self.registrace_do - dnes
			stripped_dny = str(dny_do_nove_registrace).split(" ",1)[0] + " d."
		return stripped_dny


	@property
	def Dny_do_nove_zav_registrace_csar(self):
		dnes = date.today()
		if self.zavodni_registrace_do <= dnes:
			stripped_dny = "Zavodní registrace ČSAR vypršela."
		else:
			dny_do_nove_zav_registrace = self.zavodni_registrace_do - dnes
			stripped_dny = str(dny_do_nove_zav_registrace).split(" ",1)[0] + " d."
		return stripped_dny

	@property
	def Dny_do_nove_registrace_wrrc(self):
		dnes = date.today()
		if self.registrace_wrrc_do <= dnes:
			stripped_dny = "Registrace WRRC vypršela."
		else:
			dny_do_nove_wrrc_registrace = self.registrace_wrrc_do - dnes
			stripped_dny = str(dny_do_nove_wrrc_registrace).split(" ",1)[0] + " d."
		return stripped_dny