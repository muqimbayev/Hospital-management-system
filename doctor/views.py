from django.shortcuts import render, redirect
from home.models import Doctor, Admissions, History
from django.views import View
from .forms import Doctorforms
from django.views.generic import TemplateView
from datetime import date


class LoginDoctor(View):
    def get(self, request):
        if request.method == 'POST':
            phone_number1 = request.POST.get('phone_number1')
            password = request.POST.get('password1')
            try:
                doctor = Doctor.objects.get(phone_number=phone_number1)
                if doctor.password == password:
                    return redirect('main')
            except Doctor.DoesNotExist:
                return render(request, 'doctor/login_doctor.html', {'error_message': 'Foydalanuvchi topilmadi'})
        return render(request, 'doctor/login_doctor.html')

    def post(self, request):
        phone_number = request.POST.get('phone_number1')
        doctor = Doctor.objects.get(phone_number=phone_number)
        doctor_id = doctor.id
        request.session['doctor_id'] = doctor_id
        admission_users = Admissions.objects.filter(doctor=doctor_id)
        return render(request, 'doctor/main.html', {'admission_users': admission_users})

user_id = 0
def post(request, pk):
    try:
        global user_id
        user_id = pk
        a = Admissions.objects.get(id=pk)
        history = History.objects.filter(user_id=pk)
        return render(request, 'doctor/acc.html', {'pk': pk, 'data': a, 'history': history})
    except History.DoesNotExist:
        a = Admissions.objects.get(id=pk)
        return render(request, 'doctor/acc.html', {'pk': pk, 'data': a, 'history': None})


from django.http import HttpResponse


def doctor_submit(request):
    # if request.method == 'POST':
    doctor_id = request.session.get('doctor_id')
    appeal = request.POST.get('shikoyatlar')
    diagnosis = request.POST.get('tashxis')
    print(user_id)
    history = History(appeal=appeal, diagnosis=diagnosis, doctor_id=doctor_id, user_id=user_id)
    history.save()

    return redirect('main')
