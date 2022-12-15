import datetime 
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from hour.models import Day, Month
from hour.forms import DayForm
from .forms import RegistationForm, ProfilForm
from .models import Profile
from hour.hour_counter import counter


def homepage(request):
    if request.method == 'GET':
        return render(request, 'person_auth/index.html')
    else:
        redirect('/login/')


@login_required(login_url='/login')
def profile_change(request, user_id):
    user = request.user
    
    if request.method == 'POST':
        profile = Profile.objects.filter(user=user).first()
        form = ProfilForm(request.POST, instance=profile)
        if form.is_valid():
            profile.save()
        return redirect('person_auth:home')


@login_required(login_url='/login')
def home(request):
    today = datetime.date.today()

    if request.method == "GET":
        user = request.user
        day = Day.objects.filter(user=request.user, date=today).first()
        if day is not None:
            form = DayForm(instance=day)
        else:
            form = DayForm(initial={'date': today })
        profile = Profile.objects.filter(user=user).first()
        year = today.year
        month = today.month
        month_db = Month.objects.filter(user=request.user)
        context = {"form": form, "profile": profile, "today": today, "month_db": month_db, "month": month}
        return render(request, 'person_auth/home.html', context)
    
    else:
        form = DayForm(request.POST)
        
        if form.is_valid():
            day = form.save(commit=False)
            # find the month of that day
            month = day.date.month
            year = day.date.year
            month_db, created = Month.objects.get_or_create(user=request.user, month=month, year=year)
        
            if not Day.objects.filter(user=request.user, date = day.date):
                day.user = request.user
                day.date = today
                #conect the day with month
                day.month = month_db
                day.required, day.extra = day.working_hours()
                day.completed = day.input_validate()
                day.save()
                counter(request.user, month, year)
            else:
                day_db = Day.objects.filter(user=request.user, date = day.date).first()
                form = DayForm(request.POST, instance=day_db)
                if form.is_valid():
                    day_db.required, day_db.extra = day_db.working_hours()
                    day_db.save()
                    counter(request.user, month, year)

            return redirect('person_auth:home')


def sign_up(request):
    if request.method == "POST":
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(
                user = user,
                bio = "This is me...",
            )
            login(request, user)
            return redirect('person_auth:home')
    else:
        form = RegistationForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})
