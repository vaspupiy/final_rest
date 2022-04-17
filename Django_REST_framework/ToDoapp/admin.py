from django.contrib import admin

# Register your models here.
from ToDoapp.models import Project, TODO

admin.site.register(Project)
admin.site.register(TODO)
