import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.forms import TextInput, PasswordInput

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length= 15, help_text= '*')
    first_name = forms.CharField(max_length = 30, help_text= '*')
    last_name = forms.CharField(max_length = 30, required=False) #help_text= 'Optional')
    email = forms.EmailField(max_length=200) #help_text = 'Enter valid e-mail address')
    course = forms.CharField(max_length= 35, required= True , help_text='*')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'course',
            'password1',
            'password2'
        ]

class LogInForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput( 
    #     attrs={'class': 'form control', 'placeholder': 'Username', 'required': True}))

    # password = forms.CharField(widget=forms.PasswordInput( 
    #     attrs={'class': 'form control', 'placeholder': 'Username', 'required': True}))
    
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]