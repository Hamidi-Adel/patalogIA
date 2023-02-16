from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuestionTypeForm,CreateQuestionsForm, createImageQuestion, CreateOptionsforAQuestion, createQuesitonsWithImage,createQuesitonsWithoutImage
from .models import Questions, Questionnaire, AlternativeQuestions,QuestionWiseResult,questionsWithImages,questionsWithOutImages
from demarcate.models import demarcateQuestion
from django.http import HttpResponse
import math
from django.conf import settings
from accounts.models import User

@login_required(login_url="/accounts/login/")
def dashboard(request):
    subjects = Questionnaire.objects.only('Subject')
    userType = User.objects.get(iduser = request.user.iduser)
    
    context = {'subjects': subjects, 'Type':str(userType.usertype)}
    return render(request, 'questions/teacher/dashboard.html', context)

@login_required(login_url="/accounts/login/")
def subjects(request):
    subjects = Questionnaire.objects.only('Subject')
    userType = User.objects.get(iduser = request.user.iduser)
    context = {'subjects': subjects, 'Type':str(userType.usertype)}
    return render(request, 'questions/teacher/subjects.html', context)

@login_required(login_url="/accounts/login/")
def question(request):
    form = QuestionTypeForm(request.POST or None)
    userType = User.objects.get(iduser = request.user.iduser)
    if form.is_valid():
        if str(form.cleaned_data.get('category')) == 'Demarcate':
            return redirect('questions:demarcatePage')
        elif str(form.cleaned_data.get('category')) == 'Multiple Choice Questions':
            return redirect('questions:questionscategory')
    context = {'form':form, 'Type':str(userType.usertype)}
    return render(request, 'questions/teacher/questionType.html', context)

"""-------------------------------------------------------------------------------------------------------"""
"""Demarcate Question and Answer Section"""
@login_required(login_url="/accounts/login/")
def createDemarcate(request):
    """Process images uploaded by users"""
    form = createImageQuestion(request.POST or None)
    userType = User.objects.get(iduser = request.user.iduser)

    if request.method == "POST":
        if form.is_valid():
            form = createImageQuestion(request.POST,request.FILES)
            instance = form.save(commit=False)
            x1 = int(request.POST.get("x1"))
            y1 = int(request.POST.get("y1"))
            x2 = int(request.POST.get("x2"))
            y2 = int(request.POST.get("y2"))
            getArea = findarea(x1,x2,y1,y2)
        
            instance.x = x1
            instance.y = y1
            instance.w = (x2 - x1)
            instance.h = (y2 - y1)
            instance.area = getArea
            instance.save()
        #createPoints.save()
        else:
            print(form.errors)
    return render(request, 'questions/teacher/demarcatePage.html', {'form':form, 'Type':str(userType.usertype)})

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

        # print(getDetail.x - x1)
        # print(getDetail.y - y1)
        # print(getDetail.area - getArea)
        # print(getDetail.w - w)
        # print(getDetail.h - h)

        getTheQuestionInstance = demarcateQuestion.objects.get(idmarks = pk)
        if 'marks' not in request.session:
            request.session['marks'] = getTheQuestionInstance.questionMarks
        if 'tries' not in request.session:
            request.session['tries'] = 0

        if (x1 in x_range) and (y1 in y_range) and (w in w_range) and (h in h_range) and (getArea in area_range):
            saveFinalMarks = QuestionWiseResult(questionLink = getTheQuestionInstance, marksObtain = str(request.session['marks']))
            saveFinalMarks.save()

            print(request.session['marks'])
            print(request.session['tries'])

            del request.session['marks']
            del request.session['tries']
            return redirect('questions:congrats')
            #print("Answer is Correct")
        else:
            request.session['tries'] += 1
            calculateTheDecrement = (float(request.session['marks']) - ((float(request.session['marks']) * 20)/100) * int(request.session['tries']))
            request.session['marks'] = calculateTheDecrement
            
            print(request.session['marks'])
            print(request.session['tries'])

            if request.session['tries'] >= 3:
                request.session['marks'] = 0.0
                    
                print("Final Marks: " + str(request.session['marks']))
                print("Final Tries: " + str(request.session['tries']))
                
                saveFinalMarks = QuestionWiseResult(questionLink = getTheQuestionInstance, marksObtain = str(request.session['marks']))
                saveFinalMarks.save()
                del request.session['marks']
                del request.session['tries']

                return redirect('home:StartPage')
            return redirect('questions:tryagain')
    return render(request, 'questions/student/demarcatequestiondetail.html', context)


def congrats(request):
    return render(request, 'questions/student/congo.html')

def tryagain(request):
    return render(request, 'questions/student/tryagain.html')

"""-------------------------------------------------------------------------------------------------------"""

def MCQs(request):
    form = CreateQuestionsForm(request.POST or None)
    userType = User.objects.get(iduser = request.user.iduser)

    if form.is_valid():
        form.save()
        return redirect('questions:createOptions')
    context = {'form':form, 'Type':str(userType.usertype)}
    return render(request, 'questions/teacher/MCQsPage.html', context)

def createOptions(request):
    form = CreateOptionsforAQuestion(request.POST or None)
    userType = User.objects.get(iduser = request.user.iduser)
    if form.is_valid():
        form.save()
    context = {'form':form, 'Type':str(userType.usertype)}
    return render(request, 'questions/teacher/createoptions.html', context)


def showQuestions(request):
    # descQuesiton = Questions.objects.all()
    descQuestion = questionsWithImages.objects.all()
    otherQuestion = questionsWithOutImages.objects.all()
    AllQuestions = demarcateQuestion.objects.all()
    
    context = {'QuestionText':descQuestion,'otherQuestion':otherQuestion, 'AllQuestions':AllQuestions}
    return render(request, 'questions/student/quiz.html', context)

def quizdetail(request, pk):
    # getOptions = AlternativeQuestions.objects.filter(questoes_questoes_id__description = pk)
    # rightAns = Questions.objects.get(description = pk)
    # getQuestion = pk

    questionAndOptions = questionsWithImages.objects.get(idQuestion = pk)
    context = {'Question':questionAndOptions}
    if request.method == "POST":
        selectedOptionA = request.POST.get('A')
        selectedOptionB = request.POST.get('B')
        selectedOptionC = request.POST.get('C')
        selectedOptionD = request.POST.get('D')

        if selectedOptionA == questionAndOptions.rightAnswerOfQuestion:
          
            return redirect('questions:congrats')
        elif selectedOptionB == questionAndOptions.rightAnswerOfQuestion:
           
            return redirect('questions:congrats')
        elif selectedOptionC == questionAndOptions.rightAnswerOfQuestion:
           
            return redirect('questions:congrats')
        elif selectedOptionD == questionAndOptions.rightAnswerOfQuestion:
         
            return redirect('questions:congrats')

    return render(request, 'questions/student/questionwithoptions.html', context)


def withoutimagequizdetial(request, pk):
    # getOptions = AlternativeQuestions.objects.filter(questoes_questoes_id__description = pk)
    # rightAns = Questions.objects.get(description = pk)
    # getQuestion = pk

    questionAndOptions = questionsWithOutImages.objects.get(idQuestion = pk)
    context = {'Question':questionAndOptions}
    if request.method == "POST":
        selectedOptionA = request.POST.get('A')
        selectedOptionB = request.POST.get('B')
        selectedOptionC = request.POST.get('C')
        selectedOptionD = request.POST.get('D')

        if selectedOptionA == questionAndOptions.rightAnswerOfQuestion:
          
            return redirect('questions:congrats')
        elif selectedOptionB == questionAndOptions.rightAnswerOfQuestion:
           
            return redirect('questions:congrats')
        elif selectedOptionC == questionAndOptions.rightAnswerOfQuestion:
           
            return redirect('questions:congrats')
        elif selectedOptionD == questionAndOptions.rightAnswerOfQuestion:
         
            return redirect('questions:congrats')

    return render(request, 'questions/student/withoutimgquizdetail.html', context)

def totalMarks(request, pk):
    context = {'subjectname': pk}
    return render(request, 'questions/teacher/totalMarks.html', context)

def funImageQuestion(request):
    form = createQuesitonsWithImage(request.POST or None)
    userType = User.objects.get(iduser = request.user.iduser)
    context = {'form':form, 'Type':str(userType.usertype)}

    if form.is_valid():
        form = createQuesitonsWithImage(request.POST,request.FILES)
        form.save()
    return render(request, 'questions/teacher/ImageQuestion.html', context)

def funwithoutImageQuestion(request):
    form = createQuesitonsWithoutImage(request.POST or None)
    userType = User.objects.get(iduser = request.user.iduser)
    context = {'form':form, 'Type':str(userType.usertype)}

    if form.is_valid():
        form = createQuesitonsWithoutImage(request.POST,request.FILES)
        form.save()
    return render(request, 'questions/teacher/withoutimageQuestion.html', context)

def funshowimgwithoutimgcategory(request):
    if request.method == 'POST':
        if request.POST.get("question_category") == "A":
            return redirect('questions:createImageQuestion')
        
        elif request.POST.get("question_category") == "B":
            return redirect('questions:createwithoutImageQuestion')
    return render(request, 'questions/teacher/imgwthotimgctg.html')