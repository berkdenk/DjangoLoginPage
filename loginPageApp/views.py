from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html', {'alert_message': 'Login Success!'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    request.session['logout_message'] = 'Logout Success!'  # Başarılı çıkış uyarı mesajı
    return redirect('index')  # Çıkış yapıldıktan sonra 'login' sayfasına yönlendirme
  # Çıkış yapıldıktan sonra 'login' sayfasına yönlendirme

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Başarılı kayıt durumunda 'login' sayfasına yönlendirme
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
