from django.urls import path, include
from vocab.views import home, login, dictionary, test_func

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('dictionary/', dictionary, name="dictionary"),
    path('test/', test_func)
]

