from django.urls import path
from .views import LoginDoctor, post, doctor_submit

urlpatterns = [
    path('login/', LoginDoctor.as_view(), name='doctor_login'),
    path('acc/<int:pk>/', post, name='acc'),
    path('doctor_submit/', doctor_submit, name='doctor_submit'),
    path('main/', LoginDoctor.as_view(), name='main'),  # To'g'ri
]
