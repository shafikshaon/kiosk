__author__ = 'Shafikur Rahman'
from django.contrib.auth.models import Group

from gist.models import Activity, TimeLog, Key


class Role(Group, TimeLog, Key, Activity):
    class Meta:
        db_table = 'kiosk_roles'

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,

    @classmethod
    def get_order_by_columns(cls):
        return ['name:Role name', 'is_active:Status', 'add_by:Created by', 'add_at:Created at']

    @classmethod
    def get_searchable_columns(cls):
        return ['name:Role name', 'is_active:Status', 'add_by:Created by', 'add_at:Created at:date']
