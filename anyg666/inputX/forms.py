from django.forms import modelformset_factory
from .models import Input

InputFormSet = modelformset_factory(
    Input, fields=("content", ), extra=1
)