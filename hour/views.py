import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

from .models import Day
from .forms import DayForm

# Create your views here.
class Home(LoginRequiredMixin, View):
    def get(self, request):
        days = Day.objects.filter(user=request.user)
        form = DayForm()
        context = {'days': days, 'form': form}
        return render(request, 'hour/home.html', context)

    def post(self, request):
        form = DayForm(request.POST)
        if form.is_valid():
            day = form.save(commit=False)
            print(type(day.date))
            if not Day.objects.filter(user=request.user, date = day.date):
                day.user = request.user
                day.required, day.extra = day.working_hours()
                day.completed = day.input_validate()
                day.save()
            else:
                day_db = Day.objects.filter(user=request.user, date = day.date).first()
                form = DayForm(request.POST, instance=day_db)
                if form.is_valid():
                    day_db.required, day_db.extra = day_db.working_hours()
                    day_db.completed = day_db.input_validate()
                    day_db.save()
            return redirect('hour:home')


class UpdateDay(LoginRequiredMixin, View):

    def post(self, request, day_id):
        day = Day.objects.filter(id=day_id, user=request.user)

        data = json.loads(request.body)

        # handle empty time filds - it is allowed
        start = None if data.get('start') == "" else data.get('start')
        lunch_in = None if data.get('lunch_in') == "" else data.get('lunch_in')
        lunch_out = None if data.get('lunch_out') == "" else data.get('lunch_out')
        end = None if data.get('end') == "" else data.get('end')
  
        day.update(start=start, lunch_in=lunch_in, lunch_out=lunch_out, end=end)
        required, extra = day.first().working_hours()
        completed = day.first().input_validate()
        day.update(required=required, extra=extra, completed=completed)
        
        return JsonResponse({
            "day": day.first().serialize()
        })

    def get(self, request, day_id):
        day = Day.objects.filter(id=day_id, user=request.user).first()
        day_view = day.serialize()

        return JsonResponse({
            'day_view': day_view
        })

        

class DeleteDay(LoginRequiredMixin, View):

    def post(self, request, day_id):
        day = get_object_or_404(Day, id=day_id, user=request.user)
        day.delete()
        return redirect('hour:home')


        



