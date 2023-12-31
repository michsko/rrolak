from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
from datetime import timedelta
import time


Klub = User


def platnost():
	return datetime.now().date()+ timedelta(days=365)


# Create your models here.


class Profil(models.Model):
	klub = models.OneToOneField(Klub, on_delete=models.SET_NULL, null=True)
	logo_klub = models.ImageField(upload_to='klub_logo', default='csar_logo/logo_csar.jpeg')
	info = models.TextField(blank=True)
	adresa = models.CharField(max_length=255, blank=True)
	email = models.CharField(max_length=255, blank=True)
	telefon = models.CharField(max_length=255, blank=True)
	aktivni = models.BooleanField(default=True)

	def __str__ (self):
		return self.klub.username 



class Tanecnik(models.Model):
	klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True)
	foto_tanecnik = models.ImageField('Fotografie', upload_to='foto_tanecnik/profil_foto/', default='foto_tanecnik/pic.jpg')
	jmeno = models.CharField('Jméno', max_length=255, blank=False)
	prijmeni = models.CharField('Příjmení',max_length=255, blank=False)
	datum_narozeni = models.DateField('Datum narození', blank=False)
	rodne_cislo = models.IntegerField('Rodné číslo', blank=False, unique=True)
	email = models.EmailField('Email', blank=False)
	adresa = models.TextField('Adresa', blank=True, null=True)
	telefon = models.CharField('Telefonní číslo', max_length=255, blank=False)
	zdravotni_prohlidka = models.DateField('Zdravotní prohlídka DO ', blank=False)
	zdravotni_prohlidka_potvr = models.FileField('Zdravotní prohlídka', upload_to='zdravotni_prohlidka/', null=True, blank=True)
	pas = models.FileField('Kopie pasu', upload_to='kopie_pasu/', null=True, blank=True)
	doping = models.FileField('Dopingove prohlašení', upload_to='dopingove_prohlaseni/', null=True, blank=True)
	registr_csar = models.BooleanField('Registrace csar', default=False, null=True)
	datum_registrace = models.DateField(auto_now_add=True, null=True, blank=True)
	registrace_do = models.DateField(default=platnost, null=True, blank=True)
	registr_zavodni_csar = models.BooleanField('Zavodni registrace', default=False, null=True)
	datum_zavodni_registrace_csar = models.DateField(auto_now_add=True, null=True, blank=True)
	zavodni_registrace_do = models.DateField(default=platnost, null=True, blank=True)
	registr_wrrc = models.BooleanField('Registrace wrrc', default=False, null=True)
	datum_registrace_wrrc = models.DateField(auto_now_add=True, null=True, blank = True)
	registrace_wrrc_do = models.DateField(default=platnost, null=True, blank=True)
	tanecnik = models.BooleanField('Tanečník', default=False, blank=True, null=True)
	trener = models.BooleanField('Trenér', default=False, blank=True, null=True)
	porotce = models.BooleanField('Porotce', default=False, blank=True, null=True)
	odborny_dozor = models.BooleanField("Odborný dozor", default=False, blank=True, null=True)


	def __str__(self):
		return self.jmeno + " " + self.prijmeni + " d.n " + str(self.datum_narozeni) + " r.c " + str(self.rodne_cislo)


	@property
	def Dny_do_nove_registrace_csar(self):
		today = datetime.now().date()
		dnes = today.strftime('%Y-%m-%d')
		registrace = self.registrace_do.strftime('%Y-%m-%d')

		if registrace < dnes:
			stripped_dny = "Registrace ČSAR vypršela."
			return stripped_dny

		else:
			return self.registrace_do


	@property
	def Dny_do_nove_zav_registrace_csar(self):
		today = datetime.now().date()
		dnes = today.strftime('%Y-%m-%d')
		registrace = self.zavodni_registrace_do.strftime('%Y-%m-%d')

		if registrace < dnes:
			stripped_dny = "Zavodní registrace ČSAR vypršela."
			return stripped_dny

		else:
			return self.zavodni_registrace_do
	"""	dnes = date.today()
		if self.zavodni_registrace_do <= dnes:
			stripped_dny = "Zavodní registrace ČSAR vypršela."
		else:
			dny_do_nove_zav_registrace = self.zavodni_registrace_do - dnes
			stripped_dny = str(dny_do_nove_zav_registrace).split(" ",1)[0] + " d."
		return stripped_dny
"""

	@property
	def Dny_do_nove_registrace_wrrc(self):
		today = datetime.now().date()
		dnes = today.strftime('%Y-%m-%d')
		registrace = self.registrace_wrrc_do.strftime('%Y-%m-%d')

		if registrace < dnes:
			stripped_dny = "Registrace WRRC vypršela."
			return stripped_dny

		else:
			return self.registrace_wrrc_do
	"""	dnes = date.today()
		if self.registrace_wrrc_do <= dnes:
			stripped_dny = "Registrace WRRC vypršela."
		else:
			dny_do_nove_wrrc_registrace = self.registrace_wrrc_do - dnes
			stripped_dny = str(dny_do_nove_wrrc_registrace).split(" ",1)[0] + " d."
		return stripped_dny
	"""
		

	def check_rc(self):
		rc_length = len(str(self.rodne_cislo))
		rodne_c = str(self.rodne_cislo)
		digits = []
		check = 1

		for digit in rodne_c:

				digits.append(int(digit))

				together = sum(digits)
				check = together % 11 

		if rc_length == "10" or rc_length == "9" and check == 0:
			
			return "Rodné číslo je v pořádku."


		else: 
			return "Rodné číslo neodpovídá standartní délce nebo formátu rodného čísla."


	def save(self, *args, **kwargs):
		self.check_rc()
		super(Tanecnik, self).save(*args, **kwargs)



class Tanecni_jednotka(models.Model):
	KATEGORIE = [('Děti', 'Kategorie Děti'), 
	('Žáci', 'Kategorie Žáci'),
	('Junior', 'Kategorie Junior'),
	('C', 'Kategorie C'),
	('B', 'Kategorie B'),
	('A', 'Kategorie A'),
	('MDFD', 'Malá Dívčí Formace Děti'),
	('MDFJ', 'Malá Dívčí Formace Junior'),
	('MDFS', 'Malá Dívčí Formace Senior'),
	('DFD', 'Dívčí Formace Děti'),
	('DFJ', 'Dívčí Formace Junior'),
	('DFS', 'Dívčí Formace Senior'),
	('PFJ', 'Párová Formace Junior'),
	('PFS', 'Párová Formace Senior'),
	('DG', 'Duo Girls'),
	('DL', 'Duo Ladies'),
	('BW', 'Boogie Woogie'), 
	('FSm', 'Formace smíšený věk'),]


	klub = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)
	jmeno_tanecni_jednotky = models.CharField('Jméno taneční jednotky', max_length=255, blank=True, null=True)
	kategorie = models.CharField('Kategorie', max_length=128, choices = KATEGORIE, null=True)
	tanecnici = models.ForeignKey(Tanecnik, on_delete=models.SET_NULL, null=True)
	
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
	kategorie_bw = models.BooleanField('Boogie Woogie', default=False, blank=True, null=True)
	kategorie_fsm = models.BooleanField('Formace smíšený věk', default=False, blank=True, null=True)

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
