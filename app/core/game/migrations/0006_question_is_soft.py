# Generated by Django 4.2 on 2024-06-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0005_alter_question_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="is_soft",
            field=models.BooleanField(default=True),
        ),
    ]