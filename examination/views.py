from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import Faculties.models as f
import random
import user_profiles.models as up
import time

# Create your views here.

def test(request):
    course = f.Courses.objects.all()
    user_profile = get_object_or_404(UserProfile, user = request.user)
    department_courses = f.Department_Courses.objects.get(department = user_profile.dept)
    
    related_courses = department_courses.courses.all()
    print(related_courses)
    for i in related_courses:
        print(i.course)

    tup = []
    for unit in related_courses:
        tup.append(unit.course)
        tup = sorted(tup)
    return render(request, "examination/test.html", {'tup':tup})

def exam(request): 
    if request.method == "POST":
        global objective_questions, time1, course
        time1 = int(time.time())
        mode = request.POST['mode']
        course = request.POST['course']
        type_ = request.POST['type']
        qstn_number = int(request.POST['qstn_number'])
        time_ = int(request.POST['time'])

        course = get_object_or_404(f.Courses, course = course)

        
        objective_questions = Objectives.objects.all().filter(course = course)
        objective_questions = list(objective_questions)
        random.shuffle(objective_questions)

        theory_questions = Theory.objects.all().filter(course = course)
        if (mode == "Exam Mode" and type_ == "Objective") or\
                (mode == "Study Mode" and type_ == "Objective") or \
            (mode == "Study Mode" and type_ == "Theory"):

            return render(request,'examination/exam.html', context={
                    'questions':objective_questions[:qstn_number],
                    'theory_questions': theory_questions,
                    'course':course,
                    'mode':mode,
                    'type':type_,
                    'time':time_,
                    "qstn_number": qstn_number
                })
        else:
            return redirect("test")
    else:
        return redirect("test")


def result(request):
    if request.method == "POST":
        global objective_questions
        user_profile = get_object_or_404(UserProfile, user = request.user)
        qstn_number = int(request.POST['qstn_number'])
        time2 = int(time.time())- time1
        score = 0
        wrong = 0
        total = 0
        for abc in objective_questions:
            total += 1
            if abc.correct_option == request.POST.get(abc.question):
                score+=1
            else:
                wrong+=1
        hours = time2 // 3600
        minutes = (time2 % 3600) // 60
        seconds = (time2 % 3600) % 3600
        percentage = score/qstn_number * 100
        user_profile.total_exams_taken += 1
        user_profile.total_marks += percentage
        user_profile.time_spent = time2 #In seconds
        user_profile.save()
        
        context={
            "score": score,
            'wrong': wrong,
            'total':total,
            'questions': objective_questions,
            "course": course,
            "time": f"{hours:02d} : {minutes:02d} : {seconds:02d}"
        }
        return render(request,'examination/result.html', context)
    else:
        return render(request,"examination/result.html")


def theory_explanations(request, pk):

    if request.method == "POST":
        comment = request.POST["comment"]

        theory_id = Theory.objects.get(id = pk)
        comment_theory_model = CommentTheory.objects.create(username = request.user, question = theory_id, content = comment)
        user_profile = get_object_or_404(UserProfile, user = request.user)
        comment_theory_model.user_profile = user_profile
        comment_theory_model.save()
        return redirect("/theory/explanation/"+pk)
    else:
        theory_comments = CommentTheory.objects.filter(question = pk)[::-1]
        theory = Theory.objects.get(id = pk)
        context = {
            'theory': theory,
            'theory_comments': theory_comments
        }
        return render(request, "examination/theory_explanation.html", context)
    

def objectives_explanations(request, pk):

    if request.method == "POST":
        comment = request.POST["comment"]

        objective_id = Objectives.objects.get(id = pk)
        comment_objective_model = CommentObjective.objects.create(username = request.user, question = objective_id, content = comment)
        user_profile = get_object_or_404(UserProfile, user = request.user)
        comment_objective_model.user_profile = user_profile
        comment_objective_model.save()
        return redirect("/objective/explanation/"+pk)
    else:
        objective_comments = CommentObjective.objects.filter(question = pk)[::-1]
        objective = Objectives.objects.get(id = pk)
        context = {
            'objective': objective,
            'objective_comments': objective_comments
        }
        return render(request, "examination/objective_explanation.html", context)