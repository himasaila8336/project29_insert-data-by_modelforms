from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic is inserted successfully')
    return render(request,'insert_topic.html',d)     



def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage is inserted successfully')
    return render(request,'insert_webpage.html',d)         



def AccessRecord(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('accessrecord is inserted successfully')
    return render(request,'accessrecord.html',d)         
