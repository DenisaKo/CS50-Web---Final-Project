from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    random_sequence = models.CharField(max_length=10, default="john")
    # pic = models.URLField(default=f"https://avatars.dicebear.com/api/initials/{user}.svg")
    bio = models.TextField()

    PICTURE_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('human', 'Human'),
        ('identicon', 'Identicon'),
        ('initials', 'Initials'),
        ('bottts', 'Bottts'),
        ('avataaars', 'Avataaars'),
        ('jdenticon', 'Jdenticon'),
        ('gridy', 'Gridy'),
        ('micah', 'Micah'),
    )
    pic_first = models.CharField(choices=PICTURE_CHOICE, default='male', max_length=20)

    DEPARTMENT_CHOICE = (
        ('TECH', 'tech'),
        ('ACOUNING', 'acounting'),
        ('ENVIRO', 'enviro'),
        ('WAREHOUSE', 'warehouse'),
        ('QUALITY', 'quality')
    )
    department = models.CharField(choices=DEPARTMENT_CHOICE, default='TECH', max_length=30)


