from django.contrib import admin
from .models import Day, SickHour, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Day)
admin.site.register(SickHour)
# admin.site.register(Message)
# admin.site.register(ChatterRoom)
# admin.site.register(Like)
