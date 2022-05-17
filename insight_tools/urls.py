from django.urls import path, include
from .views import *

urlpatterns = [
  path('mainpage', insights_page, name='insights_mainpage'),
  path('generate', text_generate, name='text_generate'),
  path('insightsform', insights_form_processing, name='insights_form')
]