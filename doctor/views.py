from django.shortcuts import render, redirect
from home.models import Doctor, Admissions, History, Financial
from django.views import View
from .forms import Doctorforms
from django.views.generic import TemplateView
from datetime import date
from django.contrib.auth.hashers import check_password


def LoginDoctor(request):
    if request.method == 'POST':
        phone_number1 = request.POST.get('phone_number1')
        request.session['phone_number1'] = phone_number1
        password = request.POST.get('password1')

        try:
            doctor = Doctor.objects.get(phone_number=phone_number1)
            if check_password(password, doctor.password):
                return redirect('main')
            else:
                return render(request, 'doctor/login_doctor.html', {'error_message': 'Noto‘g‘ri parol'})
        except Doctor.DoesNotExist:
            return render(request, 'doctor/login_doctor.html', {'error_message': 'Foydalanuvchi topilmadi'})

    return render(request, 'doctor/login_doctor.html')
def MainDoctor(request):
    phone_number = request.session.get('phone_number1')
    if phone_number:
        try:
            doctor = Doctor.objects.get(phone_number=phone_number)
            doctor_id = doctor.id
            request.session['doctor_id'] = doctor_id
            admission_users = Admissions.objects.filter(doctor=doctor)
            return render(request, 'doctor/main.html', {'admission_users': admission_users})
        except Doctor.DoesNotExist:
            return render(request, 'doctor/login_doctor.html', {'error_message': 'Foydalanuvchi topilmadi'})
    else:
        return render(request, 'doctor/login_doctor.html', {'error_message': 'Foydalanuvchi topilmadi'})


user_id = 0


def post(request, pk):
    try:
        global user_id
        user_id = pk
        a = Admissions.objects.get(id=pk)
        phone = a.phone_number
        print(phone)
        history = History.objects.filter(user_phone_number=phone)
        print(history)

        return render(request, 'doctor/acc.html', {'pk': pk, 'data': a, 'history': history})
    except History.DoesNotExist:
        a = Admissions.objects.get(id=pk)
        return render(request, 'doctor/acc.html', {'pk': pk, 'data': a, 'history': None})


from django.http import HttpResponse


def doctor_submit(request):
    doctor_id = request.session.get('doctor_id')
    appeal = request.POST.get('shikoyatlar')
    diagnosis = request.POST.get('tashxis')
    Admissions_true = Admissions(id=user_id)
    admissions_true = Admissions.objects.get(id=user_id)
    admissions_true.accepted = True
    phone_number = admissions_true.phone_number
    admissions_true.save()
    history = History(appeal=appeal, diagnosis=diagnosis, doctor_id=doctor_id, user_id=user_id,
                      user_phone_number=phone_number)
    history.save()

    return redirect('main')

def Accountant(request):
    financial_objects = Financial.objects.all()
    datel = []
    context_list = []
    for fin in financial_objects:
        name = fin.user_full_name
        doctor = Doctor.objects.get(id=fin.doctor_id)
        doctor_name = doctor.full_name
        price = fin.price
        date = fin.date
        datel.append(date)
        payment_type = fin.payment_type
        check_number = fin.check_number
        phone_number = fin.phone_number
        context_list.append({
            'id': fin.id,
            'full_name': name,
            'doctor_name': doctor_name,
            'price': price,
            'date': date,
            'payment_type': payment_type,
            'check_number': check_number,
            'phone_number': phone_number
        })

    return render(request, 'accoutant.html', {'financial_list': context_list})
