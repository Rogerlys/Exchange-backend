from django.db.models.query import QuerySet
from .serializers import ModuleSerializer, UniversitySerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Module, University
import json

# Create your views here.
class ModuleView(APIView):
    serializer_class = ModuleSerializer
    lookup_url_kwarg = 'nus_module_code'

    def get(self, request, format='None'):
        nus_module_code = request.GET.get(self.lookup_url_kwarg)
        if nus_module_code != None:
            module = Module.objects.filter(nus_module_code = nus_module_code)
            if module.exists():
                data = ModuleSerializer(module[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response({'Module Not Found':'Invalid Module Code.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'module code parameter not found in request'}, status.HTTP_400_BAD_REQUEST)

class UpdateModel(APIView):
    serializer_class = ModuleSerializer

    def get(self, request, format='None'):

        with open('api/data/data.json', 'r') as f:
            my_json_obj = json.load(f)

        for mapping in my_json_obj.values():
            module = Module.objects.filter(nus_module_code = mapping.get('NUS Module 1'))
            if not module.exists():
                model = Module()
                model.nus_module_code = mapping.get('NUS Module 1')
                model.nus_module_title = mapping.get('NUS Module 1 Title')
                model.nus_module_credit = int(float(mapping.get('NUS Mod1 Credits')))
                model.save()

        with open('api/data/universitydata.json', 'r') as f:
            my_json_obj = json.load(f)

        for countries in my_json_obj:
            for entries in my_json_obj[countries]:
                university = University.objects.filter(partner_university = entries.get('University'))
                if not university.exists():
                    model = University()
                    model.partner_university = entries.get('University')
                    model.partner_information = entries.get('Link')
                    model.partner_country = countries
                    model.save()

        return Response({'Database updated'}, status=status.HTTP_200_OK)
        
            

    


    