from django.db import models


class NameFromUrl(models.Model):
	variable = models.CharField(max_length = 200)

	def __str__(self):
		return self.variable




# Create your models here.
