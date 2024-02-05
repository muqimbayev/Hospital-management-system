from django.urls import path
from .views import AccoutantLogin, Accountant_info

urlpatterns = [
    path('login/', AccoutantLogin, name='accoutant_login'),
    path('info/', Accountant_info, name='accoutant'),
]