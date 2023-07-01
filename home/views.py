from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

class MainView(View):
    def get(self, request, *args, **kwargs):
        samples = [
            {
                'name': 'hello',
                'href': 'hello/',
                'description': 'A very simple view that says hello :)'
            },
            {
                'name': 'autos',
                'href': 'autos/',
                'description': 'Autos CRUD'
            }
        ]
        ctx = {
            'samples': samples
        }
        return render(request, 'home/samples.html', ctx)
