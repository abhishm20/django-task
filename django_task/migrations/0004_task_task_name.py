# -*- coding: utf-8 -*-
# Generated by Django 4.1.5 on 2023-09-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_task", "0003_remove_task_error_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="task_name",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
