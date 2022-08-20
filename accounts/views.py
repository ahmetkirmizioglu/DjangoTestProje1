from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
# from .models import UserProfile

# Create your views here.

class change_password_view(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_message = "Şifreniz Değiştirildi"
    success_url = reverse_lazy('accounts:profile')

def profile_view(request):

    if request.user.is_authenticated:
        context = {
            'isim': 'user',

    }
    else:
        context = {
            'isim': 'quest',

    }
    return render(request, 'accounts/profile.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'Giriş'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        tip = form.cleaned_data.get('tip')

        user.set_password(password)
        user.save()
        # UserProfile.objects.created(user=user)

        new_user = authenticate(username = user.username, password=password)
        login(request, new_user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'Üye Ol'})
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('home')