from django.shortcuts import render, redirect
from .forms import QuestionTypeForm,CreateQuestionsForm,CreateQuestionnaireForm, createImageQuestion
from .models import Questions, Questionnaire, AlternativeQuestions
from demarcate.models import demarcate,demarcateQuestion
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import math


def dashboard(request):
    subjects = Questionnaire.objects.only('Subject')
    context = {'subjects': subjects}
    return render(request, 'questions/teacher/dashboard.html', context)





def subjects(request):
    subjects = Questionnaire.objects.only('Subject')
    context = {'subjects': subjects}
    return render(request, 'questions/student/subjects.html', context)



def question(request):
    form = QuestionTypeForm(request.POST or None)
    if form.is_valid():
        if str(form.cleaned_data.get('category')) == 'Demarcate':
            return redirect('questions:demarcatePage')
        elif str(form.cleaned_data.get('category')) == 'Multiple Choice Questions':
            return redirect('questions:MCQsPage')
    context = {'form':form}
    return render(request, 'questions/teacher/questionType.html', context)\

"""-------------------------------------------------------------------------------------------------------"""
"""Demarcate Question and Answer Section"""
@csrf_exempt
def createDemarcate(request):
    """Process images uploaded by users"""
    form = createImageQuestion(request.POST or None)
    if request.method == "POST":
        form = createImageQuestion(request.POST, request.FILES)
        instance = form.save(commit=False)
        x1 = int(request.POST.get("x1"))
        y1 = int(request.POST.get("y1"))
        x2 = int(request.POST.get("x2"))
        y2 = int(request.POST.get("y2"))
        getArea = findarea(x1,x2,y1,y2)
        #createPoints  = demarcateQuestion(x = x1, y = y1, w = (x2 - x1), h = (y2 - y1), area = getArea, idimage = instance)
        instance.x = x1
        instance.y = y1
        instance.w = (x2 - x1)
        instance.h = (y2 - y1)
        instance.area = getArea
        instance.save()
        #createPoints.save()
    return render(request, 'questions/teacher/demarcatePage.html', {'form':form})

def findarea(x1,x2,y1,y2):
    wSqrOfX =  (x2-x1) ** 2
    wSqrOfY = (y2-y1) ** 2
    sumOfSquares = wSqrOfX + wSqrOfY
    area = math.sqrt(sumOfSquares)
    return int(area)

def demarcateQuiz(request):
    getQuestions = demarcateQuestion.objects.all()
    context = {'AllQuestions':getQuestions}
    return render(request,'questions/student/demarcatequestions.html', context)

def demarcateQuizDetail(request,pk):
    getDetail = demarcateQuestion.objects.get(idmarks = pk)
    context = {'question':getDetail}

    if request.method == "POST":
        x1 = int(request.POST.get("x1"))
        y1 = int(request.POST.get("y1"))
        x2 = int(request.POST.get("x2"))
        y2 = int(request.POST.get("y2"))
        getArea = findarea(x1,x2,y1,y2)
        w = (x2 - x1)
        h = (y2 - y1)

        threshold = 30
        
        x_range = range((getDetail.x-threshold),(getDetail.x+threshold),1)
        y_range = range((getDetail.y-threshold),(getDetail.y+threshold),1)
        w_range = range((getDetail.w-threshold),(getDetail.w+threshold),1)
        h_range = range((getDetail.h-threshold),(getDetail.h+threshold),1)
        area_range = range((getDetail.area-threshold),(getDetail.area+threshold),1)

        print(getDetail.x - x1)
        print(getDetail.y - y1)
        print(getDetail.area - getArea)
        print(getDetail.w - w)
        print(getDetail.h - h)
        if (x1 in x_range) and (y1 in y_range) and (w in w_range) and (h in h_range) and (getArea in area_range):
            print("Answer is Correct")
        else:
            print("Ansewr is Wrong")

    return render(request, 'questions/student/demarcatequestiondetail.html', context)

"""-------------------------------------------------------------------------------------------------------"""

def MCQs(request):
    form = CreateQuestionsForm(request.POST or None)
    if form.is_valid():
        print('MCQ Created')
        form.save()
    context = {'form':form}
    return render(request, 'questions/teacher/MCQsPage.html', context)

def showQuestions(request):
    descQuesiton = Questions.objects.all()
    context = {'QuestionText':descQuesiton}
    return render(request, 'questions/student/quiz.html', context)

def quizdetail(request, pk):
    getOptions = AlternativeQuestions.objects.filter(questoes_questoes_id__description = pk)
    rightAns = Questions.objects.get(description = pk)
    getQuestion = pk
    context = {'Question':getQuestion,'Options': getOptions}

    if request.method == "POST":
        selectedOptionA = request.POST.get('A')
        selectedOptionB = request.POST.get('B')
        selectedOptionC = request.POST.get('C')
        selectedOptionD = request.POST.get('D')

        if selectedOptionA == rightAns.certain:
            print('A Your Answer is correct')
            return HttpResponse('Your Answer is Correct')
        elif selectedOptionB == rightAns.certain:
            print('B Your Answer is correct')
            return HttpResponse('Your Answer is Correct')
        elif selectedOptionC == rightAns.certain:
            print('C Your Answer is correct')
            return HttpResponse('Your Answer is Correct')
        elif selectedOptionD == rightAns.certain:
            print('D Your Answer is correct')
            return HttpResponse('Your Answer is Correct')

    return render(request, 'questions/student/questionwithoptions.html', context)
