from django.db import models
from django.contrib.auth import get_user_model


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

	def __str__ (self):
		return self.klub.username