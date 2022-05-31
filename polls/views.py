from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
# Create your views here.

def index(request):
    # Question테이블의 가장 최근 데이터 5개를 받아서 latest_question_list에 저장
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 각 질문을 , 로 엮고 output 변수에 저장
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output);


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
