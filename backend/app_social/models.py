from django.conf import settings
from django.db import models


class Creator(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="creator_user",
    )


class Content(models.Model):
    "Generated Model"
    title = models.TextField()
    description = models.TextField(
        null=True,
        blank=True,
    )


# Create your models here.
