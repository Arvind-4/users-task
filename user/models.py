import uuid
from django.db import models

# Create your models here.


class Manager(models.Model):
    manager_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manager_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.manager_name if self.manager_name else "Manager"


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=False,
        blank=False,
    )
    full_name = models.CharField(max_length=255)
    mob_num = models.CharField(max_length=14, unique=True)
    pan_num = models.CharField(max_length=10, unique=True)
    manager = models.ForeignKey(
        Manager, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
