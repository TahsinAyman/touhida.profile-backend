# Generated by Django 4.1.2 on 2022-10-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
                ('designation', models.CharField(max_length=2000)),
                ('photo', models.ImageField(upload_to='static/comments/')),
            ],
        ),
    ]