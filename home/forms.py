from django import forms
from .models import Admissions

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Admissions
        fields = ('phone_number', 'full_name', 'date_birth', 'date', 'doctor')

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=True)
        if commit:
            user.save()
        return user

