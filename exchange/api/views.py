from django.db.models.fields import NullBooleanField
from django.db.models.query import QuerySet
from .serializers import ModuleSerializer, UniversitySerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status, generics
from .models import Module, University, ModulePair
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
class ModuleView(APIView):
    serializer_class = ModuleSerializer
    lookup_url_kwarg = 'nus_module_code'
    renderer_classes = [JSONRenderer]

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['indent'] = 4
        return context

    def get(self, request, format='None'):
        nus_module_code = request.GET.get(self.lookup_url_kwarg)
        if nus_module_code != None:
            module = Module.objects.filter(nus_module_code = nus_module_code)
            if module.exists():
                data = ModuleSerializer(module[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response({'Module Not Found':'Invalid Module Code.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'module code parameter not found in request'}, status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        print(request.data)
        data = [
    "[{'University': 'Hong Kong University of Science & Technology', 'Total Mappable': 1, 'Country': 'Hong Kong', 'Modules': [{'Module': 'CM1121', 'Title': 'Organic Chemistry 1', 'Credits': '4', 'Partner Modules': [{'Module Code': 'CHEM2110', 'Module Title': 'Organic Chemistry I', 'Module Credits': '3'}, {'Module Code': 'CHEM2111', 'Module Title': 'Fundamentals of Organic Chemistry', 'Module Credits': '3'}]}]}, {'University': 'Arizona State University', 'Total Mappable': 1, 'Country': 'USA', 'Modules': [{'Module': 'CM1121', 'Title': 'Organic Chemistry 1', 'Credits': '4', 'Partner Modules': [{'Module Code': 'CHM231', 'Module Title': 'ELEMENTARY ORGANIC CHEMISTRY', 'Module Credits': '3'}]}]}]",
    "[{'University': 'Hong Kong University of Science & Technology', 'Total Mappable': 1, 'Country': 'Hong Kong', 'Modules': [{'Module': 'CM1121', 'Title': 'Organic Chemistry 1', 'Credits': '4', 'Partner Modules': [{'Module Code': 'CHEM2110', 'Module Title': 'Organic Chemistry I', 'Module Credits': '3'}, {'Module Code': 'CHEM2111', 'Module Title': 'Fundamentals of Organic Chemistry', 'Module Credits': '3'}]}]}, {'University': 'Arizona State University', 'Total Mappable': 1, 'Country': 'USA', 'Modules': [{'Module': 'CM1121', 'Title': 'Organic Chemistry 1', 'Credits': '4', 'Partner Modules': [{'Module Code': 'CHM231', 'Module Title': 'ELEMENTARY ORGANIC CHEMISTRY', 'Module Credits': '3'}]}]}]"
]
        return Response(data, status=status.HTTP_200_OK)

class UniversityView(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        queryset = University.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(partner_university = name)
        return queryset
        
class ModulePage(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer
    def get_queryset(self):
        queryset = Module.objects.all()
        return queryset

class UpdateModel(APIView):
    serializer_class = ModuleSerializer

    def get(self, request, format='None'):

        with open('api/data/data.json', 'r') as f:
            my_json_obj = json.load(f)

        for mapping in my_json_obj.values():
            module = Module.objects.filter(nus_module_code = mapping.get('NUS Module 1'))
            code = mapping.get('NUS Module 1')
            title = mapping.get('NUS Module 1 Title')
            faculty = mapping.get('Faculty')
            credits = mapping.get('NUS Mod1 Credits')
            if code != "" and title != "" and faculty != "" and credits != "":
                if not module.exists():
                    model = Module()
                    model.nus_module_code = code
                    model.nus_module_title = title
                    model.nus_module_faculty = faculty
                    model.nus_module_credit = int(float(credits))
                    model.save()
                else:
                    module.update(nus_module_title = title)
                    module.update(nus_module_faculty = faculty)
                    module.update(nus_module_credit = int(float(credits)))

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
        
        with open('api/data/data.json', 'r') as f:
            my_json_obj = json.load(f)
        ModulePair.objects.all().delete()
        for mapping in my_json_obj.values():
            model = ModulePair()
            model.nus_module_code = mapping.get('NUS Module 1')
            model.partner_university = mapping.get('Partner University')
            model.partner_module_code = mapping.get('PU Module 1')
            model.partner_module_credit = mapping.get('PU Mod1 Credits')
            model.nus_module_title = mapping.get('NUS Module 1 Title')
            uniList = University.objects.filter(partner_university = model.partner_university)
            if len(uniList) > 0:
                model.partner_country = uniList[0].partner_country
            else:
                model.partner_country = 'Singapore'
            model.save()

        return Response({'Database updated'}, status=status.HTTP_200_OK)

@csrf_exempt
def getUniMatched(request, *args, **kwargs):
    result = {}
    if request.method == 'POST':
        json_body = json.loads(request.body.decode("utf-8"))
        infomation = json_body["information"]
        modules = infomation['modules']
        for mod in modules:
            partnerUnis = ModulePair.objects.filter(nus_module_code = mod)
            for pu in partnerUnis:
                try:  # If this fails it means the uni has not been installed in results
                    result[pu.partner_university]['Total Mappable'] += 1
                except KeyError as err:
                    result[pu.partner_university] = {"University": pu.partner_university,
                                  "Total Mappable": 1,
                                  "Country": pu.partner_country,
                                  "Modules": []}
                finally:
                    item = {"Module": mod,
                            "Title": pu.nus_module_code,
                            "Credits": pu.partner_module_credit,
                            "Partner Modules": pu.partner_module_code}

                    result[pu.partner_university]["Modules"].append(item)
    return JsonResponse(result)
