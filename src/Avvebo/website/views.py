
from django.shortcuts import render
from django.forms import *
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def route(request,template, model=None, object_list=None,context=None):
    #template=context['template']
    #print('{}'.format(model.objects.all())) #works!.
    #dict = {'object_list':object_list}
    #context = RequestContext(request,dict)
    if request.POST.get('from_email'): # got a post request from the contact_form
        send_email(request)
        context={'email_just_sent':True}
    return render(request=request,template_name=template,context=context)

def send_email(request):
    '''
        Default template to send an email
    '''
    msg = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    try:
        send_mail('Avvebo Form Inquiry', msg, 'gnmartinezedu@hotmail.com' , [from_email])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    #return route(request,'index.html', None, None,context=context) #HttpResponseRedirect('')#'/contact/thanks/')
    
