from django.urls import path

from authapp.views import login, register

app_name = 'mainapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),

    # .../auth/login/
    # .../auth/register/
]