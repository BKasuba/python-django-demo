from django import forms
from demo_app.models import Cars
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"   # NOTE: the trailing comma is required

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2") #Django has built in password confirmation, password2 is not stored, only used for confirmation
