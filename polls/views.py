from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
from django.template import loader
# Create your views here.

def index(request):
    # Question테이블의 가장 최근 데이터 5개를 받아서 latest_question_list에 저장
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template 불러오고 저장된 변수에 있는 값 렌더링
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
