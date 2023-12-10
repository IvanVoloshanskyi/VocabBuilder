from django.shortcuts import render


def home(request):
    return render(request, "register/register.html", )


def login(request):
    return render(request, "login/login.html",)


def dictionary(request):
    return render(request, "vocab_templates/dictionary.html")


def test_func(request):
    return render(request, 'test_template.html')