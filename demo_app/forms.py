from django import forms
from demo_app.models import Cars

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"   # NOTE: the trailing comma is required
