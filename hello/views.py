from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        html = '''
        <html>
            <body>
                <header style="text-align: center;">
                    <h1>Hello</h1>
                </header>
            </body>
        </html>
        '''
        return HttpResponse(html)
