# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choice
from django.template import loader
def index(request):
#    return HttpResponse("Hello world,you are at the polls")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ','.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',{'latest_question_list':latest_question_list})
def detail(request,question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
       
#def results(request,question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
def vote(request,question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
#        return HttpResponse(response % selected_choice.votes)
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
# Create your views here.
