# -*- coding: utf-8 -*-
# Generated by Django 4.1.5 on 2023-10-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_task", "0005_task_remark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="task_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
