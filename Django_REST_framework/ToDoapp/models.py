from django.db import models
from uuid import uuid4

from users.models import User


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False,
                           verbose_name='id')
    name = models.CharField(max_length=64, verbose_name='project_name')
    link = models.URLField(verbose_name='repository_link')
    worker = models.ManyToManyField(User, verbose_name='worker')

    class Meta:
        db_table = 'project'
        verbose_name = 'Project'

    def __str__(self):
        return f'{self.name}'


class TODO(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False,
                           verbose_name='id')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='todo_author')
    project = models.ForeignKey(
        Project,
        verbose_name='project',
        on_delete=models.CASCADE,
        related_name='todo_project'
    )
    title = models.CharField(max_length=300, verbose_name='title')
    text = models.TextField(verbose_name='text')
    created_add = models.DateTimeField(verbose_name='created_add',
                                       auto_now_add=True)
    updated_add = models.DateTimeField(verbose_name='updated_add',
                                       auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'todo'
        verbose_name = 'TODO'

    def __str__(self):
        return f'TODO {self.title} by {self.author}'
