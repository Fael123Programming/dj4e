from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class DumpPython(View):
    def get(self, request, *args, **kwargs):
        response = '<pre>\nUser data in Python:\n\n'
        response += 'Login url: ' + reverse('login') + '\n'
        response += 'Logout url: ' + reverse('logout') + '\n'
        if request.user.is_authenticated:
            response += 'User: ' + request.user.username + '\n'
            response += 'E-mail: ' + request.user.email + '\n'
        else:
            response = 'User is not logged in\n'
        response += '\n</pre>\n<a href="/authz">Go back</a>'
        return HttpResponse(response)
      
            
class ProtectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authz/main.html')
    