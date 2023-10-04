from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question #importing the question model from models.py
from django.template import loader, RequestContext
from django.urls import reverse
#used to display the content in the browser
# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    #we got question object so now we have to get the question text from it
    #output=",".join(q.question_text for q in latest_questions) 
    #we r joining the question text with comma
    
    contex={'latest_questions':latest_questions}
    return render(request,'polls/index.html',contex)  #passing context data to the template,template name- polls/index.html                   
    #return HttpResponse(template.render(context)) #passing context data to the template

def details(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    question=Question.objects.get(pk=question_id)
    return render(request,'polls/details.html',{'question':question})
def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id) #get_object_or_404 is used to get the object from the database and it needs two arguments and they are kclass and primary key
    return render(request,'polls/results.html',{'question':question})
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_question=question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'polls/details.html',{'question':question,'error_message':"You didn't select a choice"})
    else:
        selected_question.votes+=1
        selected_question.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #go to results page and we are passing question id to it
#we created a variable called question_id and each question that we created in database should be set to this variable in url