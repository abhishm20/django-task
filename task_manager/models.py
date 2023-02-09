# -*- coding: utf-8 -*-
import time

from django.db import models
from django.db.models import JSONField
from django_extra.core.models import AbstractModel

from .constants import TaskStatus


class Task(AbstractModel):
    id = models.CharField(editable=False, unique=True, primary_key=True, max_length=36)
    identifier = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20, default=TaskStatus.PENDING, choices=TaskStatus.choices
    )
    arguments = JSONField(blank=True, null=True)
    keyword_argument = JSONField(blank=True, null=True)
    return_value = models.CharField(max_length=100, blank=True, null=True)
    exception = models.JSONField(max_length=100, blank=True, null=True)
    counter = models.IntegerField(default=1)

    created_at = models.CharField(max_length=32, null=True, default=None)
    updated_at = models.CharField(max_length=32, null=True, default=None)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = int(time.time())
        self.updated_at = int(time.time())
        super().save(*args, **kwargs)
