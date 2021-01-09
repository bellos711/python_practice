# Generated by Django 2.2.4 on 2020-09-17 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favbookapp', '0002_auto_20200916_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploaded_by_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_uploaded', to='favbookapp.User'),
        ),
    ]
