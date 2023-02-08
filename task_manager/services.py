# -*- coding: utf-8 -*-
from django_extra.core.services import BaseService

from .models import Task
from .serializers import TaskSerializer


class TaskService(BaseService):
    serializer = TaskSerializer
    model = Task
