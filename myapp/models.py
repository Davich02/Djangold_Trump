from django.db import models

status_modes = [
    ('New', 'New'),
    ('In progress', 'In progress'),
    ('Pending', 'Pending'),
    ('Blocked', 'Blocked'),
    ('Done', 'Done'),
]


class Task(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category')
    status = models.CharField(max_length=20, choices=status_modes, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_manager_task"
        ordering = ['-created_at']
        verbose_name = "Task"
        verbose_name_plural = 'Tasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title')
        ]

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_modes, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_manager_subtask"
        ordering = ['-created_at']
        verbose_name = "SubTask"
        verbose_name_plural = 'SubTasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_subtask_title')
        ]

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name')
        ]

    def __str__(self):
        return self.name