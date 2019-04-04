from django.contrib import admin
from task.models import Task
# Register your models here.

class DisplayTask(admin.ModelAdmin):
    list_display = ('task','state',)

admin.site.register(Task, DisplayTask)