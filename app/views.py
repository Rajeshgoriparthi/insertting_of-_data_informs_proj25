from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        To.save()
    return render(request,'insert_topic.html')


def insert_webpage(request):
    Lot=Topic.objects.all()
    d={'Tdata':Lot}
    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['name']
        url=request.POST['url']
        To=Topic.objects.get_or_create(topic_name=tn)[0]

        Wo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url)[0]
        Wo.save()
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    Lot=Topic.objects.all()
    d={'Tdata':Lot}
    if request.method=='POST':
        name=request.POST['name']
        tn=request.POST['tn']
        pt=request.POST['pt']
        mail=request.POST['mail']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        Ao=AccessRecord.objects.get_or_create(name=name,topic_name=To,playtype=pt,email=mail)[0]
        Ao.save()
    return render(request,'insert_accessrecord.html',d)