# Generated by Django 4.1.7 on 2023-03-08 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
