from django.urls import path
from .views import InputListView, InputAddView

urlpatterns = [
    path('', InputListView.as_view(), name='input_list'),
    path('add', InputAddView.as_view(), name='add_input'),
]