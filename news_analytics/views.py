from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.

def news_page(request):
  return render(request,'news_insights.html')

def news_form_processing(request):
    if request.method == 'POST':
      news_form = newsAnalyticsForm(request.POST, request.FILES)
      if news_form.is_valid():
        news_form.save()
      
    return HttpResponseRedirect(reverse('news_mainpage'))