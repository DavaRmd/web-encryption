from django.http import HttpRequest
from django.views  import View
from django.shortcuts import render
from authentication.models import User

# Create your views here.

class DashboardView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        user_fullname = request.session.get('user_fullname')
        return render(request, 'dashboard.html', {'user_fullname': user_fullname})


