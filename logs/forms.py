from django import forms
from .models import *

class LogForm(forms.ModelForm):
    status = forms.CharField(
        required=True
    )

    description = forms.CharField(
        required=True
    )

    class Meta:
        model = Log
        fields = ['status', 'description']