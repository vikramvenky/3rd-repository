from django.urls import path
from app1.views import *
app_name='something1'


urlpatterns=[
    path('1/',fun1,name='1'),
    path('2/',fun2,name='2'),

    
]
