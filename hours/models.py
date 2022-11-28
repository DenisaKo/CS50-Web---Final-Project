from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    department = models.CharField(max_length=200)


class Day(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="days")
    date = models.DateField(blank=True)
    start = models.TimeField(blank=True)
    lunch_in = models.TimeField(blank=True)
    lunch_out = models.TimeField(blank=True)
    end = models.TimeField(blank=True)

    def serialize(self):
        return {
            "user": self.User.id,
            'user_name': self.User.username,
            'date': self.date,
            'start': self.start,
            'lunch_in': self.lunch_in,
            'lunch_out': self.lunch_out,
            'end': self.end,
        }

    def working_hours(self):
        end_minutes = self.end.hour*60 + self.end.minute
        start_minutes = self.start.hour*60 + self.start.minute
        lunch_in_minutes = self.lunch_in.hour*60 + self.lunch_in.minute
        lunch_out_minutes = self.lunch_out.hour*60 + self.lunch_out.minute
        lunch = (lunch_out_minutes - lunch_in_minutes) / 60
        total = (end_minutes - start_minutes) / 60 - lunch
        required = 8

        if total <= required:
            required = total
            extra = 0
        else:
            extra = total - required

        return {
            "required": required,
            'extra': extra
        }   


class SickHour(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sickHours")
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()


# class ChatterRoom(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, related_name="chatter_rooms_owner")
#     members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="chatter_rooms_member")


# class Message(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="messages_send")
#     recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages_received")
#     text = models.TextField()
#     chatter_room = models.ForeignKey(ChatterRoom, on_delete=models.CASCADE, related_name='messages')

# class Like(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="messages_send")
#     message = models.ForeignKey(Message,  on_delete=models.CASCADE, related_name="liked_messages")

