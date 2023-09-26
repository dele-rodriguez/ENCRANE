from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    if request.method == "POST":
        ask = request.POST["text"]

        if not ask.strip():
            return redirect("/")
        post_question = PostQuestion.objects.create(username = request.user, post = ask)
        user_profile = get_object_or_404(UserProfile, user = request.user)
        post_question.user_profile = user_profile
        user_profile.posts += 1
        post_question.save()
        user_profile.save()
        return redirect("/")
    
    recent_posts = PostQuestion.objects.all()
    # my_posts = PostQuestion.objects.filter(user_profile = user_profile)
    context = {
        # 'my_posts': my_posts[::-1],
        'recent_posts': recent_posts[::-1]
    }
    return render(request, "userblog/home.html", context)



def question(request, pk):
    if request.method == "POST":
        user_profile = get_object_or_404(UserProfile, user = request.user)
        comment = request.POST["text"]

        if not comment.strip():
            print("Error")
            return redirect("/"+pk)
        question_id = PostQuestion.objects.get(id = pk)
        question_model = Comment.objects.create(username = request.user, question = question_id, content = comment)
        user_profile = get_object_or_404(UserProfile, user = request.user)
        question_model.user_profile = user_profile
        user_profile.comments += 1
        question_model.save()
        user_profile.save()
        return redirect("/question/"+pk)
    else:
        comments = Comment.objects.filter(question = pk)[::-1]
        question_ = PostQuestion.objects.get(id = pk)
        context = {
            'question': question_,
            'comments': comments
        }
        return render(request, "userblog/question.html", context)

def contact(request):
    if request.method == "POST":
        username = request.user.username
        email = request.user.email
        message = request.POST["message"]

        if not message.strip():
            return redirect("/contact")
        contact = Contact.objects.create(name = username, email = email, review = message)
        contact.save()
        return redirect("/contact")
    return render(request, "userblog/contact.html")