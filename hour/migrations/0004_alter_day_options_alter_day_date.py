# Generated by Django 4.1.3 on 2022-12-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hour', '0003_alter_day_end_alter_day_extra_alter_day_lunch_in_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
