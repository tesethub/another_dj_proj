from django.shortcuts import render
from django.http import Http404
from django.contrib import auth
import mainApp.models as MyModule
from django.db.models import Q
from mainApp.models import *
from countViews.views import *
import datetime

TODAY=datetime.date.today()

# Create your views here.
def get_smth_by_id(request,modelname, some_id):
    try:
        smth=MyModule.__dict__[modelname].objects.get(id=some_id)
    except:
        raise Http404
    if hasattr(smth, 'active') and smth.active==False:
        raise Http404
    if hasattr(smth, 'views') :
        if views(request, modelname, some_id):
            smth.views+=1
            smth.save()
    return {'smth':smth}

def index(request, cat_id=None):
    current=Event.objects.filter(Q(date_of_start=TODAY, active=True, date_of_finish=None)|Q(date_of_start__lte=TODAY, active=True, date_of_finish__gte=TODAY))
    coming= Event.objects.filter(date_of_start__gt=TODAY, active=True).order_by('date_of_start')
    categories=CategoriesEvents.objects.all()
    if cat_id:
        current=current.filter(category__id=cat_id)
        coming=coming.filter(category__id=cat_id)
    #output={'current':current, 'coming':coming, 'categories':categories}
    output={'categories':categories, 'content':[{'name':'Текущие события', 'data':current}, {'name':'Планируемые', 'data':coming} ]}
    return render(request,'index.html', output)

def show_event(request, event_id):

    return render(request,'event.html' , get_smth_by_id(request,'Event', event_id))

def events_current(request):
    #user=auth.get_user(request).username
    return render(request,'page2.html' )

def events_coming(request):
    #user=auth.get_user(request).username
    return render(request,'page2.html' )

def events_recent(request):
    MONTH_AGO=TODAY+datetime.timedelta(days=-30)
    recent=Event.objects.filter(
        date_of_start__range=(MONTH_AGO, TODAY+datetime.timedelta(days=-1)), active=True)
    output={'content':[{'name':'Недавние события', 'data':recent}]}
    return render(request,'index.html', output)

def events_archiv(request):
    MONTH_AGO=TODAY+datetime.timedelta(days=-30)
    archiv=Event.objects.filter(
        date_of_start__lte=MONTH_AGO, active=True).order_by('-date_of_start')
    output={'content':[{'name':'Архив', 'data':archiv}]}
    return render(request,'index.html', output)


def places(request, cat_id=None):
    places_list=Place.objects.all()
    categories=CategoriesPlaces.objects.all()
    if cat_id:
        places_list=places_list.filter(category__id=cat_id)
    return render(request,'places.html' ,{'places':places_list, 'categories':categories})

def show_place(request, place_id):
    return render(request,'place.html',  get_smth_by_id(request,'Place', place_id) )



def articles(request):
    articles=Article.objects.filter(active=True).order_by('added')
    return render(request,'articles.html' ,{'articles':articles})



def show_article(request, article_id):
    return render (request,'article.html', get_smth_by_id(request,'Article', article_id))