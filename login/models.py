from django.db import models

class User(models.model):
	email = models.Charfield(max_length=250)
	password = models.Charfield(max_length=250)
	mobile_number = models.Charfield(max_length=250)
		