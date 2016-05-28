from django.db import models

# Create your models here.

class Dosya(models.Model):
	dosya_adi = models.TextField()
	arsa_sahibi = models.TextField()
	yapimci_firma = models.TextField()
	araci_firma = models.TextField()
	ek_notlar = models.TextField()
	il = models.TextField()
	ilce = models.TextField()
	belediye = models.TextField()
	pafta = models.TextField()
	ada = models.TextField()
	parsel = models.TextField()
	kayit_tarihi = models.DateTimeField(auto_now_add=True, auto_now=False)
	guncelleme_tarihi = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode_(self):
		return self