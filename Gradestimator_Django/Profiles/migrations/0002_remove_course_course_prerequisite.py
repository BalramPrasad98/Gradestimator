# Generated by Django 2.2.2 on 2020-05-26 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Course_PreRequisite',
        ),
    ]