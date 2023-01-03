from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from users.models import User


class Status(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_tasks"
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    assignee = models.ManyToManyField(
        User, related_name="assignee_tasks", null=True,
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_tasks')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Picture(models.Model):
    task = models.ForeignKey(
        Task, related_name="images", on_delete=models.CASCADE
    )
    image = models.FileField(
        null=True,
        blank=False,
        upload_to="images/",
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])],
    )

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"

    def __str__(self):
        return self.task.title