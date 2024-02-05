from django.urls import path
from .views import LoginDoctor, post, doctor_submit, MainDoctor

urlpatterns = [
    path('login/', LoginDoctor  , name='doctor_login'),
    path('acc/<int:pk>/', post, name='acc'),
    path('doctor_submit/', doctor_submit, name='doctor_submit'),
    path('main/', MainDoctor, name='main'),
]
