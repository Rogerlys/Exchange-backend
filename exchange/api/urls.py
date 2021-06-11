from django.urls import path
from .views import ModuleView, UpdateModel, UniversityView, ModulePage, getUniMatched

urlpatterns = [
    path('modules', ModulePage.as_view()),
    path('module-view', ModuleView.as_view()),
    path('update-model', UpdateModel.as_view()),
    path('university-view', UniversityView.as_view()),
    path('university-matched', getUniMatched)
]
