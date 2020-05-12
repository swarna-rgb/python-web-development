from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader
from django.shortcuts import render
def welcome(request):
    output = ""
    """latest_question_list = Question.objects.order_by('-pub_date')[:5]
    for question in latest_question_list:
        output += question.question_txt + ',' 
         return HttpResponse(output) """

    """latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    #context is a dictionary mapping template varibale names to python oobjects
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html', context)


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    context = {'question':question}
    return render(request, 'polls/detail.html', context )

def result(request, question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    response = "you're voting on question %s"
    return HttpResponse(response % question_id)