from django.urls import path
from .views import AccoutantLogin, Financial_info
urlpatterns = [
    path('login/', AccoutantLogin, name='accoutant_login'),
    path('info/', Financial_info, name='accoutant'),
]




