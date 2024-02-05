from django.urls import path
from .views import HomePages, Admin_login, Admin_panel, Signup, About_doctor, Payment
from doctor.views import Accountant

urlpatterns = [
    path('', HomePages.as_view(), name='home'),
    path('administrator_login/', Admin_login, name='administrator_login'),
    path('admin_panel/', Admin_panel.as_view(), name='admin_panel'),
    path('signupUser/', Signup.as_view(), name='signupUser'),
    path('about_doctor/', About_doctor.as_view(), name='about_doctor'),
    path('payment/', Payment.as_view(), name='payment'),
    path('accoutant/', Accountant, name='accoutant'),
]
