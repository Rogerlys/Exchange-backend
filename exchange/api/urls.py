from django.urls import path
from .views import UpdateModel, UniversityPage, ModulePage, CountryPage, getUniMatched, getModulePairing, getPDF, getNLP

urlpatterns = [
    #returns a list of all nus modules in the database
    path('modulesOptions', ModulePage.as_view()),
    #Updates the database with new infomation
    path('update-model', UpdateModel.as_view()),
    #Get universities for the dropdown option
    path('universityOptions', UniversityPage.as_view()),
    path('countryOptions', CountryPage.as_view()),
    path('university-matched', getUniMatched),
   #Takes in a list of nus modules and a list of unis with number of mods matched
    path('module-pairing', getModulePairing),
    #Generates the pdf
    path('PDF', getPDF),
    #NLP end point
    path('nlp', getNLP),
]
