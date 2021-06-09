from rest_framework import serializers
from .models import Module, University

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('nus_module_code', 'nus_module_title', 'nus_module_credit')

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('partner_university', 'partner_information', 'partner_country')