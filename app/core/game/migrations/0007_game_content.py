# Generated by Django 4.2 on 2024-07-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0006_question_is_soft"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="content",
            field=models.JSONField(default=dict),
        ),
    ]
