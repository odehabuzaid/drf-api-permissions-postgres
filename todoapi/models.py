from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

LABEL_CHOICES = (
    ("NoLabel", "High"),
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low"),
    ("OnHold", "Hold"),
)


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        "auth.User", related_name="tasks", on_delete=models.CASCADE
    )
    task = models.CharField(max_length=20)
    label = models.CharField(max_length=10, choices=LABEL_CHOICES, default="NoLabel")
    du_date = forms.DateTimeField(widget=forms.TextInput(attrs={"type": "date"}))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(Task, self).save(*args, **kwargs)
