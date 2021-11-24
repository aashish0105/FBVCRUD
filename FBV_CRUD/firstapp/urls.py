from .views import *
from django.urls import path

urlpatterns=[
    path('add/',add_laptop,name='add'),
    path('displaylaptops/',display_laptop,name='display'),
    path('update/<int:lid>/',update_laptop,name='updt'),
    path('delete/<int:i>/',delete_laptop,name='dlt')
]