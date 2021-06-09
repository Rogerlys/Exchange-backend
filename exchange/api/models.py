from django.db import models

# Create your models here.
class Module(models.Model):
    nus_module_code = models.CharField(max_length=10, unique=True)
    nus_module_title = models.CharField(max_length=100)
    nus_module_credit = models.IntegerField(null=False)
    partner_university = models.CharField(max_length=100, unique=False, null=True)

class University(models.Model):
    partner_university = models.CharField(max_length=100, unique=True, null=False)
    partner_information = models.TextField()
    partner_country = models.CharField(max_length=20, null=False)
    