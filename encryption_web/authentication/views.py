from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from django.db.models import Q
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from authentication.models import User


# Create your views here.

class RegisterView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        if request.session.get('user_id'):
            return redirect('dashboard:index')
        return render(request, 'register.html')

    def post(self, request: HttpRequest, *args, **kwargs):
        if request.session.get('user_id'):
            return redirect('dashboard:index')
         
        # ngambil data dari form register.html
        username = request.POST.get('username')
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        no_hp = request.POST.get('no_hp')
        nip = request.POST.get('nip')
        password = request.POST.get('password')

        #validasi untuk menghindari inputan kosong
        if not all ([username, nama, email, no_hp, nip]):
            messages.error(request, 'Semua field harus diisi.')
            return render(request, 'register.html')
        
        #validasi username jika username sudah terdaftar
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, "Username atau email sudah terdaftar, Tolong gunakan yang lain.")
            return render(request, 'register.html')

        #validasi email jika email tidak valid
        try: 
            validate_email(email)

        except ValidationError:
            messages.error(request, 'Email tidak valid.')
            return render(request, 'register.html')
        
        #validasi no_hp jika no_hp sudah terdaftar
        if User.objects.filter(no_hp=no_hp).exists():
            messages.error(request, "Nomor HP sudah terdaftar.")
            return render(request, 'register.html')

        #validasi nip jika nip sudah terdaftar
        if User.objects.filter(nip=nip).exists():
            messages.error(request, "NIP sudah terdaftar.")
            return render(request, 'register.html')

        #password wajib diisi
        if not password:
            messages.error(request, "Password harus diisi.")
            return render(request, 'register.html')

        #password wajib untuk minimal 6 karakter
        if len(password) < 6: 
            messages.error(request, "Password minimal 6 karakter.")
            return render(request, 'register.html')
        
        user = User.objects.create(
            username = username,
            fullname = nama,
            email = email,
            no_hp = no_hp,
            nip = nip,
            password = make_password(password) 
        )

        messages.success(request, 'Pendafatan Berhasil, Silahkan Login.')
        return redirect('login')


class LoginView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        if request.session.get('user_id'):
            return redirect('dashboard:index')
        return render(request, 'login.html')
    

    def post(self, request: HttpRequest, *args, **kwargs):

        if request.session.get('user_id'):
            return redirect('dashboard:index')

        # ngambil data dari form login
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')


        try:
            user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email = username_or_email)
            except User.DoesNotExist:
                user = None
            
        if user is None:
            messages.error(request, "Username atau email tidak ditemukan.")
            return render(request, 'login.html')

        # Membandingkan password input dengan hash di database
        if not check_password(password, user.password):
            messages.error(request, "Password salah.")
            return render(request, 'login.html')
        
        # Login berhasil 
        request.session['user_id'] = user.id  # Menyimpan ID user yang ada di session
        request.session['user_fullname'] = user.fullname
        request.session.set_expiry(1000) # session akan dihapus setelah 30 menit 
        messages.success(request, f"Selamat datang, {user.fullname}!")
        return redirect('dashboard:index')


# Logout dengan menghapus session
class LogoutView(View):
    def get(self, request:HttpRequest, *args, **kwargs):
        request.session.flush()
        list(messages.get_messages(request))
        return redirect('authentication:login')
