# Generated by Django 4.2.13 on 2024-11-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0008_alter_category_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="label_de",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="label_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="label_fr",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="label_de",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="label_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="label_fr",
            field=models.TextField(null=True),
        ),
    ]