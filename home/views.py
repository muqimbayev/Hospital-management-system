from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Admin
from datetime import datetime
from django.views import View
from django.http import HttpRequest
from .models import Doctor, Admissions, Financial
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout

class HomePages(TemplateView):
    template_name = 'home.html'

def Admin_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(phone_number=phone_number)
            if check_password(password, admin.password):
                return redirect('admin_panel')
        except Admin.DoesNotExist:
            return render(request, 'Adm/login.html', {'error_message': 'Foydalanuvchi topilmadi'})

    return render(request, 'Adm/login.html')

class Admin_panel(TemplateView):
    template_name = 'Adm/main.html'

def get(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'Adm/signupUser.html', context)

class Signup(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        context = {'doctors': doctors}
        return render(request, 'Adm/signupUser.html', context)

    def post(self, request):
        if request.method == 'POST':
            doctor_info = request.POST['doctor']
            doctor_parts = doctor_info.split(', ')
            doctor_id = doctor_parts[0]
            request.session['doctor_id'] = doctor_id
            doctor = Doctor.objects.get(id=doctor_id)

            phone_number = request.POST['phone_number']
            request.session['phone_number'] = phone_number
            full_name = request.POST['full_name']

            request.session['full_name'] = full_name
            date_birth = request.POST['date_birth']
            datetime = request.POST['datetime']
            price = doctor_parts[-1].split()[0]
            price = request.session.get('price')

            user = Admissions(phone_number=phone_number, full_name=full_name, date_birth=date_birth,
                              doctor=doctor, date=datetime)
            user.save()
            return redirect('payment')
        return render(request, 'Adm/signupUser.html')


class Payment(View):

    def get(self, request):
        from datetime import datetime
        hozirgi_vaqt = datetime.now()
        check = [hozirgi_vaqt.year,
                 hozirgi_vaqt.month,
                 hozirgi_vaqt.day,
                 hozirgi_vaqt.hour,
                 hozirgi_vaqt.minute,
                 hozirgi_vaqt.second]
        a = lambda x: ''.join(map(str, x))

        check_number = int(a(check))
        doctor_id = request.session.get('doctor_id')
        full_name = request.session.get('full_name')
        doctor = Doctor.objects.get(id=doctor_id)
        price = doctor.price
        doctor_name = doctor.full_name
        phone_number = request.session.get('phone_number')

        context = {'price': price, 'full_name': full_name, 'check_number': check_number, 'doctor': doctor_name}
        return render(request, 'Adm/payment.html', context)

    def post(self, request):
        price = request.POST.get('price')
        doctor = request.POST.get('doctor')
        doctor_obj = Doctor.objects.get(full_name=doctor)
        doctor_id = int(doctor_obj.id)

        full_name = request.session.get('full_name')
        check_number = request.POST.get('check_number')
        phone_number = request.session.get('phone_number')
        payment_method = request.POST.get('payment_method')

        payment_info = Financial(price=price, doctor_id=doctor_id, user_full_name=full_name, check_number=check_number,
                                 phone_number=phone_number, payment_type=payment_method)
        payment_info.save()
        return redirect('signupUser')

class About_doctor(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        context = {'doctors': doctors}
        return render(request, 'Adm/about_doctor.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')


