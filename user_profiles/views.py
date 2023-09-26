from django.shortcuts import render, redirect, get_object_or_404
from user_blog.models import PostQuestion
from .models import *
from Faculties.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UserProfileForm

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        username =  (request.POST["username"]).lower()
        email =  (request.POST["email"]).lower()
        password1 =  request.POST["password1"]
        password2=  request.POST["password2"]

        if password1 != password2:
            messages.info(request, "Passwords don't match!")

        else:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already exists")
                return redirect("/register")
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email Already Exists!")
                return redirect("/register")
            elif profile_form.is_valid():
                user = User.objects.create_user(username = username, email = email, password = password1).save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                return redirect("/login")
            else:
                messages.info(request, "Incorrect Information!")

    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
        context = {
            "form": form,
            "p_form": profile_form
        }
        return render(request, "userprofiles/register.html", context)

def login_(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password_signin"]

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Incorrect Credentials!")
            return redirect("/login")

    return render(request,"userprofiles/login.html")

def logout_(request):
    logout(request)
    return redirect("/login")
    

def dashboard(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user = request.user)
        my_posts = PostQuestion.objects.filter(user_profile = user_profile)

        average_time_spent = user_profile.get_average_time()
        average_mark = user_profile.get_average_mark()
        
        context = {
            'my_posts': my_posts[::-1],
            'total_exams_taken': user_profile.total_exams_taken,
            'average_time_spent': average_time_spent,
            'average_mark': round(average_mark, 2),
            "comments": user_profile.comments,
            "posts": user_profile.posts,
            "user_profile": user_profile
        }
        return render(request, "userblog/dashboard.html", context)
    else:
        return redirect("/login")