from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('email','username', 'password',)