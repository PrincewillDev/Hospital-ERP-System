from django import forms
from .models import employee_data
from django.forms.widgets import DateInput
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

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
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
        validators=[validate_password]
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user