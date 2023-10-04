from django.urls import path
from . import views
from polls import views


#adding urls to django applications
app_name = 'polls'
urlpatterns = [
    #url(r'^$',views.index,name='index'),
    #127.0.0.1/polls - this is curent url
    #^$ means don't add anything new to the url
    #name is used to identify the view, ie its like giving it a name
    #view.index is the function that will be called if the url matches 
    #that is what we r displaying
    path('',views.index,name='index'),
    #we r calling details function - views.details [check in views.py]
    #the question_id can be from 0-9
    #127.0.0.1/polls/1 - this is curent url of questin_id 1
    
    #path('question_id[0-9]+>results/',views.results, name='results'),
    path('<int:question_id>/',views.details, name='details'),
    path('<int:question_id>/results/',views.results, name='results'),
    #the url is - 127.0.0.1/polls/1/results
    
    path('<int:question_id>/vote/',views.vote, name='vote'),
    #127.0.0.1/polls/1/vote
    
]
    
