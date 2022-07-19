from django.forms import formset_factory
from django import forms
from .models import Input


class InputForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                              label="Контент", empty_value="null")

InputFormSet = formset_factory(
    InputForm, extra=1
)
