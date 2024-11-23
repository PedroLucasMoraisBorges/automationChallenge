from django import forms
from .models import *

class DocForm(forms.ModelForm):
    docName = forms.CharField(
        required=True
    )

    author = forms.CharField(
        required=True
    )

    url = forms.CharField(
        required=False
    )

    dtRegister = forms.DateTimeField(
        required=True
    )

    score = forms.FloatField(
        required=True
    )

    class Meta:
        model=Docs
        fields = ['docName', 'author', 'url', 'dtRegister', 'score']