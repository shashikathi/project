from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from polls.models import Question, Choice

def index(request):
   
    questions = Question.objects.all()
    
    context = {
        'question_list': [question for question in questions]
    }
    
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
  
    question = Question.objects.get(id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/result.html', context)


def vote(request, question_id):
    question = Question.objects.get(id=question_id)

    try:
        selected_choice = Choice.objects.get(id=request.POST["my_selection"])

    except (KeyError, Choice.DoesNotExist):
        
        return render(request, "polls/detail.html", { "question": question, "error_message": "You didn't select a choice.",},
        )
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
       
        return HttpResponseRedirect(reverse("results", args=(question.id,)))