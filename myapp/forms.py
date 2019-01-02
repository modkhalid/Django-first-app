from myapp.models import UserInfo
from django import forms

from django.contrib.auth.models import User

class UserFormBasic(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password','email')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=('portfolioLink','profile_pic')
