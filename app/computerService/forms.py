from django import forms
from .models import *



class EmployeForm(forms.ModelForm):
        class Meta:
            model = Work_with_us
            fields = '__all__'
        



