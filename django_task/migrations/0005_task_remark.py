# -*- coding: utf-8 -*-
# Generated by Django 4.1.5 on 2023-09-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_task", "0004_task_task_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="remark",
            field=models.TextField(blank=True, null=True),
        ),
    ]
