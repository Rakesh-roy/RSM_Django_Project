import random
from Application.utils import sendOtpText
from django import forms
from Application.models import RegistrationModel


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_otp(self):
        contact = self.cleaned_data['contact']
        otp = random.randint(100000,999999)
        message = 'Hello! Welcome To Resume Management System Your One Time Password is : '+str(otp)
        sendOtpText(message,contact)
        return otp

    class Meta:
        model = RegistrationModel
        exclude= ('status',)
