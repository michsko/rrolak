from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from datetime import datetime


Klub = get_user_model()


# Create your models here.


class Profil(models.Model):
	klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True)
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
	klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True)
	foto_tanecnik = models.ImageField('Fotografie', upload_to='foto_tanecnik', default='foto_tanecnik/pic.jpg')
	jmeno = models.CharField('Jméno', max_length=255, blank=False)
	prijmeni = models.CharField('Příjmení',max_length=255, blank=False)
	datum_narozeni = models.DateField('Datum narození', blank=False)
	rodne_cislo = models.IntegerField('Rodné číslo', blank=False)
	email = models.EmailField('Email', blank=False)
	adresa = models.TextField('Adresa', blank=True, null=True)
	telefon = models.CharField('Telefonní číslo', max_length=255, blank=False)
	zdravotni_prohlidka = models.DateField('Zdravotní prohlídka DO ', blank=False)
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

class Tanecni_jednotka(models.Model):
	klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True)
	jmeno_tanecni_jednotky = models.CharField('Jméno taneční jednotky', max_length=255, blank=True, null=True)
	jmeno_tanecnik1 = models.ForeignKey(Tanecnik, related_name='tanecnik1', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik2 = models.ForeignKey(Tanecnik, related_name='tanecnik2', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik3 = models.ForeignKey(Tanecnik, related_name='tanecnik3', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik4 = models.ForeignKey(Tanecnik, related_name='tanecnik4', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik5 = models.ForeignKey(Tanecnik, related_name='tanecnik5', on_delete=models.SET_NULL, null=True, blank=True)	
	jmeno_tanecnik6 = models.ForeignKey(Tanecnik, related_name='tanecnik6', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik7 = models.ForeignKey(Tanecnik, related_name='tanecnik7', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik8 = models.ForeignKey(Tanecnik, related_name='tanecnik8', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik9 = models.ForeignKey(Tanecnik, related_name='tanecnik9', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik10 = models.ForeignKey(Tanecnik, related_name='tanecnik10', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik11 = models.ForeignKey(Tanecnik, related_name='tanecnik11', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik12 = models.ForeignKey(Tanecnik, related_name='tanecnik12', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik13 = models.ForeignKey(Tanecnik, related_name='tanecnik13', on_delete=models.SET_NULL, null=True, blank=True)
	jmeno_tanecnik14 = models.ForeignKey(Tanecnik, related_name='tanecnik14', on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.jmeno_tanecni_jednotky
	

class Zavod(models.Model):
	jmeno_souteze = models.CharField(max_length=255, blank=False, null=True)
	datum_souteze = models.DateField(null=True)
	prihlasky_do = models.DateField(null=True)
	kategorie_deti = models.BooleanField('Děti', default=False, blank=True, null=True)
	kategorie_zaci = models.BooleanField('Žáci', default=False, blank=True, null=True)
	kategorie_junior = models.BooleanField('Junior', default=False, blank=True, null=True)
	kategorie_c = models.BooleanField('C', default=False, blank=True, null=True)
	kategorie_b = models.BooleanField('B', default=False, blank=True, null=True)
	kategorie_a = models.BooleanField('A', default=False, blank=True, null=True)
	kategorie_mdfd = models.BooleanField('Malé Dívčí Formace Děti', default=False, blank=True, null=True)
	kategorie_mdfj = models.BooleanField('Malé Dívčí Formace Junior', default=False, blank=True, null=True)
	kategorie_mdfs = models.BooleanField('Malé Dívčí Formace Senior', default=False, blank=True, null=True)
	kategorie_dfd = models.BooleanField('Dívčí Formace Děti', default=False, blank=True, null=True)
	kategorie_dfj = models.BooleanField('Dívčí Formace Junior', default=False, blank=True, null=True)
	kategorie_dfs = models.BooleanField('Dívčí Formace Senior', default=False, blank=True, null=True)
	kategorie_fj = models.BooleanField('Párová Formace Junior', default=False, blank=True, null=True)
	kategorie_fs = models.BooleanField('Párová Formace Senior', default=False, blank=True, null=True)
	kategorie_dg = models.BooleanField('Duo Girls', default=False, blank=True, null=True)
	kategorie_dl = models.BooleanField('Duo Ladies', default=False, blank=True, null=True)


	def __str__ (self):
		return self.jmeno_souteze


class Prihlaska_zavod(models.Model):
	zavod = models.ForeignKey(Zavod, on_delete=models.SET_NULL, null=True, related_name='prihlaseni')
	klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True, related_name='clen_klubu')
	kategorie = models.CharField("Kategorie", max_length=255, blank=False)
	tanecni_jednotka_jmeno = models.CharField('Jméno taneční jednotky', max_length=255, blank=True, null=True)
	tanecni_jednotka = models.ForeignKey(Tanecni_jednotka, on_delete=models.SET_NULL, null=True, blank=False)
	platba = models.BooleanField("Platba", default= False)
	datum_prihlaseni = models.DateTimeField(auto_now_add=True, null=True)
	hudba = models.FileField('Závodní hudba', upload_to='zavodni_hudba', blank=True)

	def __str__ (self):
		return self.tanecni_jednotka_jmeno + " " + str(f"platba: " + str(self.platba)) 