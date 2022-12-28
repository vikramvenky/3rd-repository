from django import path
from app2.views import *
app_name='something2'


urlpatterns=[
    path('3/','string1',name='3'),
    path('4/','string2',name='4'),

]