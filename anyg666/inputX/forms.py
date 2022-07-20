from django.forms import formset_factory
from django import forms
from .models import Input


class InputForm(forms.Form):
    content = forms.CharField(label="Input", empty_value="null")

InputFormSet = formset_factory(
    InputForm, extra=1
)
