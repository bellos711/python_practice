# Generated by Django 2.2.4 on 2020-09-20 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0002_auto_20200918_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='liked_wish',
        ),
        migrations.AddField(
            model_name='wish',
            name='users_who_liked',
            field=models.ManyToManyField(related_name='liked_wish', to='examapp.User'),
        ),
    ]
