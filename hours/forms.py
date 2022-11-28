from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import Day

# class DayForm(forms.Form):
#     User_imput = forms.CharField(max_length=64)
#     date_input = forms.DateField(widget=AdminDateWidget())
#     start_input = forms.TimeField(widget=AdminTimeWidget())
#     lunch_in_input = forms.TimeField(widget=AdminTimeWidget())
#     lunch_out_input = forms.TimeField(widget=AdminTimeWidget())
#     end_input = forms.TimeField(widget=AdminTimeWidget())


# class DayModelForm(forms.ModelForm):
    
#     class Meta:
#         model = Day
#         fields=["date", 'start',  "lunch_in", "lunch_out", "end"]
#         widgets = {
#             "date": AdminDateWidget(),
#             "start": AdminTimeWidget(),
#             "lunch_in": AdminTimeWidget(),
#             "lunch_out": AdminTimeWidget(),
#             "end": AdminTimeWidget()
#         }
