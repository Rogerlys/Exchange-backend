from api.models import Module
from django.urls import path
from .views import ModuleView, UpdateModel

urlpatterns = [
    path('module-view', ModuleView.as_view()),
    path('update-model', UpdateModel.as_view())
]
