from django.urls import path
from . import views

urlpatterns = [
    path('', views.DumpPython.as_view(), name='dump')
]