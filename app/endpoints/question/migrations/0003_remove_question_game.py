# Generated by Django 4.2 on 2023-12-21 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_question_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='game',
        ),
    ]
