from django.urls import path, include
from .views import *

urlpatterns = [
  path('mainpage', news_page),
  path('newsform', news_form_processing, name='news_form')
]