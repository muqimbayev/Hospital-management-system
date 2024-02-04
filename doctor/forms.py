from django import forms
from home.models import Doctor


class Doctorforms(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('phone_number', 'password')

    def save(self, commit=True):
        user = super(Doctorforms, self).save(commit=True)
        if commit:
            user.save()
        return user
