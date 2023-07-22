import uuid
from django.db import models

from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Group(BaseModel, models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners')
    name = models.CharField(max_length=256)
    members = models.ManyToManyField(
        User, blank=True, related_name='group')

    def __str__(self) -> str:
        return self.name


class Message(BaseModel, models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    text = models.CharField(max_length=256)
