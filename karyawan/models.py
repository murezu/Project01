from django.db import models

# Create your models here.

class jabatan(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class karyawan(models.Model):
	fullname = models.CharField(max_length=255)
	alamat = models.CharField(max_length=255)
	no_hp = models.CharField(max_length=15)
	jabatan = models.ForeignKey(jabatan,on_delete=models.CASCADE)