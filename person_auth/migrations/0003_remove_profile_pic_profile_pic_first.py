# Generated by Django 4.1.3 on 2022-12-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_auth', '0002_profile_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='pic_first',
            field=models.IntegerField(choices=[(11, 'Male'), (12, 'Female'), (13, 'Male'), (14, 'Male'), (15, 'Male'), (16, 'Male'), (17, 'Male'), (18, 'Male'), (19, 'Male'), (20, 'Male')], default=11),
        ),
    ]