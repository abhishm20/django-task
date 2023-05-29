# -*- coding: utf-8 -*-
# Generated by Django 4.1.6 on 2023-05-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0006_remove_task_exception_task_failed_reason_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=models.CharField(blank=True, default=None, max_length=32),
        ),
        migrations.AlterField(
            model_name="task",
            name="failed_reason",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="return_value",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="updated_at",
            field=models.CharField(blank=True, default=None, max_length=32),
        ),
    ]
