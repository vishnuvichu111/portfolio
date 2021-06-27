from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Book
class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120,widget=forms.PasswordInput)


class BookCreateFrom(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),

            'Subject': forms.TextInput(attrs={'class': 'form-control'}),
            'Message': forms.TextInput(attrs={'class': 'form-control'})
        }

