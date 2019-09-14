__author__ = 'Shafikur Rahman'
from django.contrib.auth.models import Group

from gist.models import Activity, TimeLog


class Role(Group, TimeLog, Activity):
    class Meta:
        db_table = 'kiosk_roles'

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,

    @classmethod
    def get_order_by_columns(cls):
        return ['name']

    @classmethod
    def get_searchable_columns(cls):
        return ['name']
