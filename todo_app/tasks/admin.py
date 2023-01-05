from django.contrib import admin
from .models import Task, Status, Picture


class PictureAdmin(admin.StackedInline):
    model = Picture


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [PictureAdmin]

    class Meta:
        model = Task


admin.site.register(Status)
