from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()

    TECH = 1
    ACOUNING = 2
    ENVIRO = 3
    WAREHOUSE = 4
    QUALITY = 5

    DEPARTMENT_CHOICE = (
        (TECH, 'tech'),
        (ACOUNING, 'acounting'),
        (ENVIRO, 'enviro'),
        (WAREHOUSE, 'warehouse'),
        (QUALITY, 'quality')
    )

    department = models.IntegerField(choices=DEPARTMENT_CHOICE, default=TECH)


class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="days")
    date = models.DateField(blank=True)
    start = models.TimeField(blank=True, null=True)
    lunch_in = models.TimeField(blank=True, null=True)
    lunch_out = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    required = models.FloatField(blank=True, null=True)
    extra = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

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
        if self.start is not None:
            # start_minutes = hour_to_min(self.start)
            if self.lunch_in is not None:
                # lunch_in_minutes = hour_to_min(self.lunch_in)
                # hours_morning = lunch_in_minutes - start_minutes
                hours_morning = hour_to_min(self.lunch_in) - hour_to_min(self.start)
                if self.lunch_out is not None:
                    # lunch_out_minutes = hour_to_min(self.lunch_out)
                    if self.end is not None:
                        # end_minutes = hour_to_min(self.end)
                        hours_evening = hour_to_min(self.end) - hour_to_min(self.lunch_out)
                        hours = hours_morning + hours_evening
                    else:
                        hours = hours_morning
                else:
                    hours = hours_morning
            else:
                if self.lunch_out is not None:
                    # lunch_out_minutes = hour_to_min(self.lunch_out)
                    if self.end is not None:
                        # end_minutes = hour_to_min(self.end)
                        hours = hour_to_min(self.end) - hour_to_min(self.lunch_out)
                    else:
                        hours = 0
                else:
                    if self.end is not None:
                        hours = hour_to_min(self.end) - hour_to_min(self.start)
                    else:
                        hours = 0
        else:
            if self.lunch_in is not None:
                if self.lunch_out is not None:
                    # lunch_out_minutes = hour_to_min(self.lunch_out)
                    if self.end is not None:
                        # end_minutes = hour_to_min(self.end)
                        hours = hour_to_min(self.end) - hour_to_min(self.lunch_out)
                    else:
                        hours = 0
                else:
                    if self.end is not None:
                        hours = 0
                    else:
                        hours = 0
            else:
                if self.lunch_out is not None:
                    # lunch_out_minutes = hour_to_min(self.lunch_out)
                    if self.end is not None:
                        # end_minutes = hour_to_min(self.end)
                        hours = hour_to_min(self.end) - hour_to_min(self.lunch_out)
                    else:
                        hours = 0
                else: 
                    if self.end is not None:
                        hours = 0
                    else:
                        hours = 0

        if hours == 0:
            required, extra = 0, 0
        else:               
            hours_h = hours / 60
            if hours_h >= 8:
                required, extra = 8, hours_h - 8
            else:
                required, extra = hours_h, 0
        return required, extra


def hour_to_min(part):
    return part.hour*60 + part.minute  


class SickHour(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sickHours")
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

