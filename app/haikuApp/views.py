from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice, Haiku


def index(request):
    question_list = Question.objects.filter()
    choice_list = Choice.objects.filter()
    context = {
        'question_list': question_list,
        'choice_list': choice_list
    }
    return render(request, 'haikuApp/index.html', context)


def result(request):
    return render(request, 'haikuApp/result.html')
