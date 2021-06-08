from api.models import Module
from django.urls import path
from .views import ModuleView, UpdateView, modulePage

urlpatterns = [
    path('module-view', ModuleView.as_view()),
    path('update-model', UpdateView.as_view()),
    path('module/', modulePage)
]
