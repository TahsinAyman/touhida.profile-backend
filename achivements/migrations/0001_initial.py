# Generated by Django 4.1.2 on 2022-10-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achivements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='static/achivements')),
                ('name', models.CharField(max_length=2000)),
                ('date', models.DateField()),
            ],
        ),
    ]
