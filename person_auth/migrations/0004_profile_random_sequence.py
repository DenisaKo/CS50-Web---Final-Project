# Generated by Django 4.1.3 on 2022-12-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_auth', '0003_remove_profile_pic_profile_pic_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='random_sequence',
            field=models.CharField(default='john', max_length=10),
        ),
    ]
