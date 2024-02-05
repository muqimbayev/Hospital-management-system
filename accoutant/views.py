from django.shortcuts import render, redirect
from home.models import Financial, Doctor, Accountant
from django.http import HttpResponse
from django.db.models import Sum
from django.contrib.auth.hashers import check_password
# Create your views here.

def AccoutantLogin(request):
    if request.method == 'POST':
        phone_number1 = request.POST.get('phone_number2')
        password = request.POST.get('password2')
        try:
            accoutant = Accountant.objects.get(phone_number=phone_number1)
            if check_password(password, accoutant.password):
                return redirect('accoutant')
        except Accountant.DoesNotExist:
            return render(request, 'accoutant/login.html', {'error_message': 'Foydalanuvchi topilmadi'})
    return render(request, 'accoutant/login.html')



def Accountant_info(request):
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
    summa = Financial.objects.aggregate(Sum('price'))
    return render(request, 'accoutant/accoutant.html', {'financial_list': context_list, 'summa': summa['price__sum']})
