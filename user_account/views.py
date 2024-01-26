from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_account.forms import CustomUserCreationForm, LoginUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect("vocab:dictionary:main_page")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("vocab:dictionary:main_page")
    else:
        form = CustomUserCreationForm()

    context = {"form": form}
    return render(request, 'register/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('user_account:login_user')


class LoginUser(LoginView):
    redirect_authenticated_user = True
    form_class = LoginUserForm
    template_name = "login/login.html"

    def get_success_url(self):
        return reverse_lazy("vocab:dictionary:main_page")
