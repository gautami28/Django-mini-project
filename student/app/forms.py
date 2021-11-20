from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class studform(forms.ModelForm):
    class Meta:
        model=Studdata
        fields=['name','clas','rollno','FEcgpa','Hobbies','Reviews']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'clas':forms.TextInput(attrs={'class':'form-control'}),
            'rollno':forms.TextInput(attrs={'class':'form-control'}),
            'FEcgpa':forms.TextInput(attrs={'class':'form-control'}),
            'Hobbies':forms.TextInput(attrs={'class':'form-control'}),
            'Reviwes':forms.TextInput(attrs={'class':'form-control'}),
        }