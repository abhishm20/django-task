# -*- coding: utf-8 -*-
import uuid

from django_extra.core.services import BaseService

from .models import Task
from .serializers import TaskSerializer


class TaskService(BaseService):
    serializer = TaskSerializer
    model = Task

    def create(self, data):
        if not data.get("identifier"):
            data["identifier"] = str(uuid.uuid4())
        return super().create(data)
