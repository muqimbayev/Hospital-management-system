from django.db import models
# Create your models here.
from django.contrib.auth.hashers import make_password

class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    date_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super(Admin, self).save(*args, **kwargs)


class Accountant(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    date_birth = models.DateField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super(Accountant, self).save(*args, **kwargs)


class Doctor(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    date_birth = models.DateField()
    password = models.CharField(max_length=128)
    price = models.IntegerField()
    gender = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name + ', ' + self.specialty


class Admissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    date_birth = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        about = self.phone_number + ', ' + self.full_name
        return about


class History(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    user_phone_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    doctor_id = models.IntegerField()
    appeal = models.TextField()
    diagnosis = models.TextField()


class Financial(models.Model):
    id = models.BigAutoField(primary_key=True)
    check_number = models.BigIntegerField(unique=True)
    user_full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    doctor_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.BigIntegerField()
    payment_type = models.CharField(max_length=50)



