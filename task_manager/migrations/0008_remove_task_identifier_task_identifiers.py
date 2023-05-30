# -*- coding: utf-8 -*-
# Generated by Django 4.1.6 on 2023-05-30 02:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "task_manager",
            "0007_alter_task_created_at_alter_task_failed_reason_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="identifier",
        ),
        migrations.AddField(
            model_name="task",
            name="identifiers",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
