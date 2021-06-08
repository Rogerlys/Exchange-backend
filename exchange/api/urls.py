from api.models import Module
from django.urls import path
from .views import ModuleView, UpdateView

urlpatterns = [
    path('module-view', ModuleView.as_view()),
    path('update-model', UpdateView.as_view())
]
