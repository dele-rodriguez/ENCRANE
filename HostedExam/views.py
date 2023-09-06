from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import * 
from django.contrib import messages
from uuid import uuid4

# Create your views here.

def home(request):

    if request.method == "POST":
        title = (request.POST["exam_name"]).lower()
        time_st = request.POST["exam_st"]
        time_end = request.POST["exam_end"]
        duration = int(request.POST["duration"])
        description = request.POST["description"]
        user = User.objects.get(username = request.user.username)

        if HostedExam.objects.filter(title = title, examiner = user).exists():
            messages.info(request, "This Exam exists!")
            return redirect("/hostexam")

        else:
            if title == False or time_st == False or time_end == False\
                or duration == False:
                messages.info(request, "Please fill out the fields!")
                return redirect("/hostexam")

            elif duration <= 0:

                messages.info(request, "Minutes must be greater than 0!")
                return redirect("/hostexam")

            else:
                exam = HostedExam.objects.create(
                    id = str(uuid4()),
                    title = title,
                    time_st = time_st,
                    time_end = time_end,
                    duration = duration,
                    description = description,
                    examiner = user
                )
                exam.save()

                return redirect("/hostexam/myexams")
    if request.user.is_authenticated:
        return render(request, "hostedexam/index.html")
    else:
        return redirect("/login")
def myexams(request):

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)

        exams_by_user = HostedExam.objects.filter(examiner=user).order_by("title")

        context = {
            'user': user,
            'exams': exams_by_user
        }

        return render(request, "hostedexam/myexams.html", context)

    else:
        return render(request, "error/not-authorized.html")

def questions(request, id):

    if request.user.is_authenticated:

        if request.method == "POST":
            del_question_id = int(request.POST["del_question"])
            question = Question.objects.get(id = del_question_id)
            question.delete()

            return redirect("/hostexam/questions/" + id)

        examiner = User.objects.get(username = request.user.username)
        if HostedExam.objects.get(id = id, examiner = examiner):

            exam = HostedExam.objects.get(id = id)
            
            questions = Question.objects.filter(exam = exam)

            if questions.count() == 0:
                empty = True
            else: 
                empty = False

            context = {
                "questions": questions,
                "empty": empty,
                "exam": exam
            }

            return render(request, "hostedexam/questions.html", context)
        else:
            return render(request, "error/not-authenticated.html")

    else:
        return render(request, "error/not-authenticated.html")

def addquestion(request, id):

    if request.user.is_authenticated:
        examiner = User.objects.get(username = request.user.username)
        exam = HostedExam.objects.get(id = id, examiner = examiner)
        if exam:

            if request.method ==  "POST":
                qstn = request.POST["qstn"]
                op1 = request.POST["op1"]
                op2 = request.POST["op2"]
                op3 = request.POST["op3"]
                op4 = request.POST["op4"]
                answer = request.POST["answer"]

                question = Question.objects.create(
                    exam = exam, question = qstn, op1 = op1, op2 = op2, op3 = op3, op4 = op4, answer = answer, examiner = examiner
                )

                question.save()

            context = {
                "exam": exam
            }
            return render(request, "hostedexam/add.html", context)
        else:
            return render(request, "error/not-authenticated.html")

    else:
        return render(request, "error/not-authenticated.html")
        