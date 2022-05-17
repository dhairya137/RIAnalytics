from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.
def social_page(request):
  return render(request,'social_media.html')

def social_form_processing(request):
    if request.method == 'POST':
      social_form = socialAnalyticsForm(request.POST, request.FILES)
      if social_form.is_valid():
        social_form.save()
      
    return HttpResponseRedirect(reverse('social_mainpage'))