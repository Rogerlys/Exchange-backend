from django.urls import path
from .views import UpdateModel, UniversityPage, ModulePage, CountryPage, getUniMatched, getModulePairing, getPDF, getNLP

urlpatterns = [
    path('modulesOptions', ModulePage.as_view()),
    path('update-model', UpdateModel.as_view()),
    path('universityOptions', UniversityPage.as_view()),
    path('countryOptions', CountryPage.as_view()),
    path('university-matched', getUniMatched),
    path('module-pairing', getModulePairing),
    path('PDF', getPDF),
    path('nlp', getNLP),
]
