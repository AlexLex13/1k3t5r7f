from django.urls import path

urlpatterns = [
    path('', InputLIstView.as_view(), name='input_list'),
    path('add', InputAddView.as_view(), name='add_input'),
]