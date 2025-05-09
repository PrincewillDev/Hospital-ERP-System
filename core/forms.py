from django import forms
from .models import employee_data
from django.forms.widgets import DateInput
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Employee_Form(forms.ModelForm):
    class Meta:
        model = employee_data
        fields = "__all__"
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'date_of_hire': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['passport_img'].widget.attrs.update({
            'accept': 'image/*',
            'class': 'form-control'
        })

class Registerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }