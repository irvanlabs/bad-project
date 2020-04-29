from django.db import models

# Create your models here.
class post(models.Model):
	judul = models.CharField(max_length=200)
	content = models.TextField()
	category = models.CharField(max_length=200)

	def __str__(self):
		return "{}. {}".format(self.id, self.judul)