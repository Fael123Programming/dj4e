from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def example(request):
    form = forms.BasicForm()
    return HttpResponse(form.as_table())


class SimpleCreate(DumpPostView):
    def get(self, request):
        form = forms.BasicForm()
        ctx = {'form': form}
        return render(request, 'form/form.html', ctx)
    

class SimpleUpdate(DumpPostView):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar',
            'mileage': 42,
            'purchase_date': '2018-08-14'
        }
        form = forms.BasicForm(old_data)
        ctx = {'form': form}
        return render(request, 'form/form.html', ctx)