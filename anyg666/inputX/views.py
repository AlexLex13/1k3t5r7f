from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from .forms import InputFormSet
from .models import Input


class InputListView(ListView):
    model = Input
    template_name = 'inputX/input_list.html'


class InputAddView(TemplateView):
    template_name = 'inputX/add_input.html'

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset = InputFormSet()
        return self.render_to_response({'input_formset': formset})

    def post(self, *args, **kwargs):
        formset = InputFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
                inp = Input(content=form.cleaned_data)
                inp.save()
            return redirect(reverse_lazy("input_list"))

        return self.render_to_response({'input_formset': formset})
