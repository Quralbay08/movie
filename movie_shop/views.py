from . import models
from django.shortcuts import render,get_object_or_404,redirect

from . import forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    kino = models.Movies.objects.all()
    return render(request,'home.html',{'kinolar':kino})


def product_detail(request,id):
    kino_d = get_object_or_404(models.Movies,id=id)
    comments = models.Comments.objects.filter(movie=kino_d)
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.movie = kino_d
            new_comment.username = request.user
            return redirect('detail',id=kino_d.id)
    else:
        comment_form = forms.CommentForm()
        return render(request,'detail.html',{
            'movie':kino_d,
            'comments':comments,
            'comment_form':comment_form
        })
        
    
    return render(request,'detail.html',{'detail':kino_d})


def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'reg.html',{'form':form})


def sing_in(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')

