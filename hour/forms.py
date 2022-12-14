from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Day, Month


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['date', 'start', 'lunch_in', 'lunch_out', 'end', 'public_holiday']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start': TimeInput(),
            'lunch_in': TimeInput(),
            'lunch_out': TimeInput(),
            'end': TimeInput(),
        }

class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ['month']