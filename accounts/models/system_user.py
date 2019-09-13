from django.contrib.auth.models import AbstractUser
from django.db import models

from gist.models import TimeLog, Activity

__author__ = 'Shafikur Rahman'


class SystemUser(AbstractUser, TimeLog, Activity):
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        app_label = 'accounts'
        db_table = 'kiosk_accounts'
        ordering = ['-add_at']
        verbose_name = "account"
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.username
