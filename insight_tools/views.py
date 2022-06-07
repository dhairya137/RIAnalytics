from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .forms import *
from RIAnalytics.settings import FILES_DIR
import os
from text_analytics.txtInsight import  TextAnalyst
# Create your views here.
info = {
  'reportFilename':'',
  'keywordFilename':'',
  'keywords':None,
}
def insights_page(request):
  return render(request, 'insights.html')

def text_generate(request):
  analyst = TextAnalyst()
  try:
    report = analyst.generateHTML(info['reportFilename'], info['keywordFilename'],info['keywords'])
    return JsonResponse({'status':'successful', 'report':report})
  except Exception as E:
    print('Error',str(E))
    return JsonResponse({'status':'Failed', 'report':''})


def handle_uploaded_file(f, filename):
    with open(os.path.join(FILES_DIR,filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def insights_form_processing(request):
    if request.method == 'POST':
      insights_form = insightsAnalyticsForm(request.POST)
      all_files = []
      my_files=request.FILES.getlist('report_files')
      if insights_form.is_valid():
          for f in my_files:
              all_files.append(f.name)
              info['reportFilename'] = f.name
              handle_uploaded_file(f, f.name)
          keyfile = request.FILES['keyword_file']
          info['keywordFilename'] = keyfile.name
          handle_uploaded_file(keyfile, keyfile.name)



          if request.is_secure():
            protocol = 'https'
          else:
            protocol = 'http'

          domain = protocol + "://" + request.META['HTTP_HOST']

          return render(request,'text_report.html', context={'mode':'Text','files':all_files, 'url': f'{domain}/text/generate','statusurl': f'{domain}/returnstatus'})
      else:
          return render(request,'text_insights.html', context={'insightsform':insights_form})

      
    return HttpResponseRedirect(reverse('insights_mainpage'))