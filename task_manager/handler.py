# -*- coding: utf-8 -*-
import celery

from .constants import TaskChoices
from .models import Task
from .services import TaskService

# pylint: disable=no-member,import-error,too-many-arguments


class TaskHandler(celery.Task):
    def run(self, *args, **kwargs):
        pass

    def before_start(self, task_id, args, kwargs):
        data = {
            "task_id": task_id,
            "status": TaskChoices.PENDING,
            "arguments": {"args": args[0]},
            "keyword_argument": kwargs,
        }
        TaskService().create(data=data)

    def on_success(self, retval, task_id, args, kwargs):
        task_instance = Task.objects.filter(task_id=task_id).first()
        TaskService(task_instance.id).update(
            data={
                "status": TaskChoices.SUCCESS,
                "arguments": {"args": args[0]},
                "keyword_argument": kwargs,
                "return_value": retval,
            }
        )

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        task_instance = Task.objects.filter(task_id=task_id).first()
        TaskService(task_instance.id).update(
            data={
                "status": TaskChoices.FAILURE,
                "arguments": {"args": args[0]},
                "keyword_argument": kwargs,
                "exception": {"Exception": exc},
            }
        )

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        task_instance = Task.objects.filter(task_id=task_id).first()
        TaskService(task_instance.id).update(
            data={
                "status": TaskChoices.PENDING,
                "arguments": {"args": args[0]},
                "keyword_argument": kwargs,
                "exception": {"Exception": exc},
                "counter": task_instance.instance.counter + 1,
            }
        )

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        task_instance = Task.objects.filter(task_id=task_id).first()
        TaskService(task_instance.id).update(
            data={
                "status": status,
                "arguments": {"args": args[0]},
                "keyword_argument": kwargs,
                "return_value": retval,
            }
        )
