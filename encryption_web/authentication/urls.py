
from django.urls import path

from authentication.views import LoginView, RegisterView, LogoutView


app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
