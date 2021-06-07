from api.models import Module
from django.urls import path
from .views import ModuleView

urlpatterns = [
    path('module-view', ModuleView.as_view())
]
