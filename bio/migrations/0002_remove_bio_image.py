# Generated by Django 3.2.13 on 2022-10-10 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='image',
        ),
    ]