from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

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
            if not Day.objects.filter(user=request.user, date = day.date):
                day.user = request.user
                day.required, day.extra = day.working_hours()
                day.save()
            else:
                day_db = Day.objects.filter(user=request.user, date = day.date).first()
                form = DayForm(request.POST, instance=day_db)
                if form.is_valid():
                    day_db.required, day_db.extra = day_db.working_hours()
                day_db.save()
            return redirect('hour:home')


class UpdateDay(LoginRequiredMixin, View):
    def post(self, request, day_id):
        day = Day.objects.filter(id=day_id, user=request.user)

        # handle empty time filds - it is allowed
        start = None if request.POST.get('start') == "" else request.POST.get('start')
        lunch_in = None if request.POST.get('lunch_in') == "" else request.POST.get('lunch_in')
        lunch_out = None if request.POST.get('lunch_out') == "" else request.POST.get('lunch_out')
        end = None if request.POST.get('end') == "" else request.POST.get('end')

        day.update(start=start, lunch_in=lunch_in, lunch_out=lunch_out, end=end)
        required, extra = day.first().working_hours()
        day.update(required=required, extra=extra)
        
        return redirect('hour:home')



class DeleteDay(LoginRequiredMixin, View):

    def post(self, request, day_id):
        day = get_object_or_404(Day, id=day_id, user=request.user)
        day.delete()
        return redirect('hour:home')



# class DetailDay(LoginRequiredMixin, View):
#     def get(self, request, day_id):
#         day = get_object_or_404(Day, id=day_id, user=request.user)
#         form = DayForm(instance=day)
#         context = {'form': form}
#         return render(request, 'hour/detail_day.html', context)

#     def post(self, request, day_id):
#         day = get_object_or_404(Day, id=day_id, user=request.user)
#         form = DayForm(request.POST, instance=day)
#         if form.is_valid():
#             day.save()
#             return redirect('hour:home')

#         context = {'form': form}
#         return render(request, 'hour/detail_day.html', context)
        



