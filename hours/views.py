from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from datetime import datetime, timedelta

from .models import Day, SickHour, Profile
# from .forms import DayModelForm

def overview(request):
    file_doc = 'static/overview.txt'
    return render(request, file_doc, content_type='text/plain')


def get_days(request):
    user = request.user
    days = Day.objects.filter(User=user)
    days_json = [day.serialize() for day in days]
    hours = [day.working_hours() for day in days]
    for i in range(len(days_json)):
        days_json[i].update(hours[i])
  
    return JsonResponse({
        'days': days_json,
    })


def index(request):
    if request.user.is_authenticated:
        if request.method == "GET" :
            user = request.user
            days = Day.objects.filter(User=user)
            days_json = [day.serialize() for day in days]
            hours = [day.working_hours() for day in days]
            for i in range(len(days_json)):
                days_json[i].update(hours[i])
          
            return render(request, "hours/index.html", {
                "days": days_json,
               
            })
        elif request.method == "POST":
            form = DayModelForm()
            return render(request, "hours/index.html", {
                'form': form
            })

    else:
        return render(request, "hours/index.html", {
            "message": "currently logged out",
        })


# @csrf_protect
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return HttpResponseRedirect(reverse('hours:index'))
#         else:
#             # Return an 'invalid login' error message.
#             return render(request, "hours/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "hours/login.html") 


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("hours:index"))


# @csrf_protect
# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "hours/register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#             profile = Profile.objects.create(pk=user.id)
#             # profile.save()
#         except IntegrityError:
#             return render(request, "hours/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("hours:index"))
#     else:
#         return render(request, "hours/register.html")
