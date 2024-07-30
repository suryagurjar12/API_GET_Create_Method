from django.urls import path
from .views import *

urlpatterns = [
    path('stu_info/<int:pk>',Stu_details,name='Stu_details'),
    path('stu_list/',Stu_list,name='Stu_list'),
    path('list/',list,name='list')
]