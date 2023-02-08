# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import JSONField
from django_extra.core.models import AbstractModel


class Task(AbstractModel):
    task_id = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50)
    status = models.CharField(max_length=20, blank=True, null=True)
    arguments = JSONField(blank=True, null=True)
    keyword_argument = JSONField(blank=True, null=True)
    return_value = models.CharField(max_length=100, blank=True, null=True)
    exception = models.JSONField(max_length=100, blank=True, null=True)
    counter = models.IntegerField(default=1)
