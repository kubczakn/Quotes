from random import choice
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Choice, Haiku


@csrf_exempt
def index(request):
    if request.method == 'POST':
        type = request.POST['c']
        if type == 'Positive':
            return redirect('positive/')

        return redirect('negative/')


    else:
        question_list = Question.objects.filter()
        choice_list = Choice.objects.filter()
        context = {
            'question_list': question_list,
            'choice_list': choice_list
        }
        return render(request, 'haikuApp/index.html', context)


def positive(request):
    haiku_list = Haiku.objects.filter(type='Positive')
    haiku = choice(haiku_list)
    context = {
        'haiku' : haiku
    }
    return render(request, 'haikuApp/positive.html', context)


def negative(request):
    haiku_list = Haiku.objects.filter(type='Negative')
    haiku = choice(haiku_list)
    context = {
        'haiku' : haiku
    }
    return render(request, 'haikuApp/negative.html', context)
