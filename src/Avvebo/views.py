'''
Created on Jan 10, 2019

@author: gabe
'''
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def home(request):
    c = {'person_name': 'John Smith',
         'product': 'Super Lawn Mower',
         'company': 'Outdoor Equipment',
         'ship_date': datetime.date(2009, 4, 2),
         'ordered_warranty': True}
    return render_to_response('index.html', c)