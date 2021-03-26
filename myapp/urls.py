from django.urls import path, re_path
from myapp.views import *


urlpatterns = [
    path('', base, name='main'),
    re_path(r'(?P<phone_number>^050\d{7}|096\d{7}|068\d{7})/$', correct_num, name='correct_num'), #phone valid
    re_path(r'(?P<some_string>^[a-f0-9]{4}\-[a-f0-9]{6})/$', correct_string, name='correct_string'),  #string valid
    path('article/<int:article_num>/', article_odd, name='article_with_int'),
    path('article/<int:article_num>/<slug:name>', article_odd, name='article_name'),
    path('users', users, name='users'),
    path('article/', article, name='article'),

]