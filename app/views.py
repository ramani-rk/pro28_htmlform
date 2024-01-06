from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models.functions import Length

def topics (request):
    TO=Topics.objects.all()
    TO=Topics.objects.all().order_by('topic_name')
    TO=Topics.objects.all().order_by('-topic_name')
    TO=Topics.objects.all().order_by(Length('topic_name'))
    TO=Topics.objects.all().order_by(Length('topic_name').desc())
    TO=Topics.objects.all()

    d={'topics' : TO}
    return render(request,'topics.html',d)

def webpage (request):
    WO=Webpage.objects.all()
    WO=Webpage.objects.all().order_by('name')
    WO=Webpage.objects.all()

    d={'webpage' : WO}
    return render (request,'webpage.html',d)

def accessrecord (request):
    AO=Accessrecord.objects.all()
    AO=Accessrecord.objects.all().order_by('author')
    AO=Accessrecord.objects.all().order_by('-author')
    AO=Accessrecord.objects.all().order_by(Length('author'))
    AO=Accessrecord.objects.all().order_by(Length('author').desc())

    d={'accessrecord' : AO}
    return render (request,'accessrecord.html',d)

def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topics.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        to=Topics.objects.all()
        d={'topics':to}
        return render(request,'topics_datas.html',d)
    return render(request,'create_topic.html')

def create_webpage(request):
    to=Topics.objects.all()
    d={'topics' : to}
    if request.method == 'POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        TO=Topics.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        wo.save()

        wp=Webpage.objects.all()
        d={'webpage':wp}
        return render(request,'webdata.html',d)
    return render(request,'create_webpage.html',d)


def create_record(request):
    wo=Webpage.objects.all()
    d={'webpage' : wo}
    if request.method == 'POST':
        na=request.POST['na']
        da=request.POST['da']
        ar=request.POST['ar']

        WO=Webpage.objects.get(name=na)
        ao=Accessrecord.objects.get_or_create(name=WO,date=da,author=ar)[0]
        ao.save()
        ap=Accessrecord.objects.all()

        d={'accessrecord':ap}
        return render(request,'recorddata.html',d)
    return render(request,'create_record.html',d)

def select_multiple_webpage(request):
    QLTO=Topics.objects.all()
    d={'topics' : QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')

        QLWO=Webpage.objects.none()
        for to in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=to)

        d1={'webpage' : QLWO}
        return render(request,'webdata.html',d1)

    return render (request,'select_multiple_webpage.html',d)

def checkbox(request):
    QLTO = Topics.objects.all()
    d={'topics' :QLTO}

    
    return render(request,'checkbox.html',d)