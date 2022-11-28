from django.shortcuts import render, redirect
from .forms import RegistationForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get('post_id')
        print(post_id)
        post = Post.objects.filter(pk=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'person_auth/home.html', {"posts": posts})


@login_required(login_url='/login')
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('person_auth:home')
    else:
        form = PostForm()

    return render(request, 'person_auth/post_create.html', {'form': form})


def sign_up(request):
    if request.method == "POST":
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('person_auth:home')
    else:
        form = RegistationForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})
