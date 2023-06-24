from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class tamil(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my2','placeholder':"Enter username"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my2','placeholder':"Enter email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2','placeholder':"Enter password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2','placeholder':"Re-Enter password"}))
    class Meta:
        model=User  
        fields=['username','email','password1','password2']
        
class inba(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my2','placeholder':"Enter username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2','placeholder':"Enter password"}))
    class Meta:
        model=User
        fields=["username","password"]