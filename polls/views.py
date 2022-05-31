from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

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
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does not exist")

    # question_id가 없는경우 404에러 발생하는 함수
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
