from django.views.generic import ListView
from .models import Input


class InputListView(ListView):
    model = Input
    template_name = 'input_list.html'
