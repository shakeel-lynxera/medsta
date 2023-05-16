import django
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

# class RegistrationForm(forms.ModelForm):
#     full_name = forms.CharField(max_length=30)
#     gender = forms.RadioSelect()
#     password = forms.PasswordInput()
#     confirm_password = forms.PasswordInput()
#     class Meta:
#         model = User
#         fields = ["full_name", "email", "gender", "password", "confirm_password"]
    
#     def clean(self):
     
#         # super(RegistrationForm, self).clean()
        
#         full_name = self.cleaned_data.get('full_name')
#         email = self.cleaned_data.get('email')
#         gender = self.cleaned_data.get("gender")
 
#         # conditions to be met for the username length
#         if len(self.password) < 8:
#             self._errors['username'] = self.error_class([
#                 'Minimum 8 characters required'])
#             return self.errors
#         # return any errors if found
#         return self.cleaned_data


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    gender = forms.RadioSelect()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

class LoginForm(forms.Form):
    email = forms.CharField(label="Email Address", max_length=100)
    password = forms.CharField(label="Password", max_length=100)
