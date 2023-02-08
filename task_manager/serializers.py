# -*- coding: utf-8 -*-
from django_extra.core.serializers import FlexFieldsModelSerializer

from .models import Task


class TaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
