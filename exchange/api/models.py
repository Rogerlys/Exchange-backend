from django.db import models

# Create your models here.
class Module(models.Model):
    nus_module_code = models.CharField(max_length=10, unique=True)
    nus_module_title = models.CharField(max_length=50)
    nus_module_credit = models.IntegerField(null=False)

class University(models.Model):
    partner_univerity = models.CharField(max_length=50, unique=True)
    partner_information = models.TextField()
    