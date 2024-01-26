from django.urls import path

from user_account.views import register, LoginUser, logout_user

app_name = 'user_account'

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', LoginUser.as_view(), name="login_user"),
    path('logout/', logout_user, name="logout_user"),

]
