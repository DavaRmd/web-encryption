from django.http import HttpRequest
from django.views  import View
from django.shortcuts import render
from authentication.models import User

# Create your views here.

class DashboardView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, 'dashboard.html')


