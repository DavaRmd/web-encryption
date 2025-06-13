from django.shortcuts import render
from django.http import HttpRequest
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, 'index.html')
