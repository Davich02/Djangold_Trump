import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
django.setup()


from django.utils import timezone
from datetime import timedelta
from myapp.models import Task,SubTask

task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline= timezone.now() + timedelta(days=2)
)


subtask1 = SubTask.objects.create(
    title="Gather information",
    task=task,
    description="Find necessary information for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=2)
)


subtask2= SubTask.objects.create(
    title="Create slides",
    task=task,
    description="Create presentation slides",
    status="New",
    deadline=timezone.now() + timedelta(days=1)
)

new_task = Task.objects.filter(status="New")
print(new_task)

expired = SubTask.objects.filter(status="Done",deadline__lt=timezone.now())
print(expired)


Task.objects.filter(title="Prepare presentation").update(status="In progress")

SubTask.objects.filter(title="Gather information").update(deadline=timezone.now()-timedelta(days=2))

SubTask.objects.filter(title="Create slides").update(description="Create and format presentation slides")

Task.objects.filter(title="Prepare presentation").delete()