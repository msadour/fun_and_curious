# Generated by Django 4.2 on 2023-12-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0003_alter_profile_managers_profile_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
