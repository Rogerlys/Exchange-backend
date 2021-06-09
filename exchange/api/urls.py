from api.models import Module
from django.urls import path
from .views import ModuleView, UpdateModel, UniversityView

urlpatterns = [
    path('module-view', ModuleView.as_view()),
    path('update-model', UpdateModel.as_view()),
    path('university-view', UniversityView.as_view()),
    path('module', modulePage.as_view()),
]
