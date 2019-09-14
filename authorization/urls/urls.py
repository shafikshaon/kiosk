from django.urls import path

from authorization.views.role import RoleAddView

__author__ = "Shafikur Rahman"

urlpatterns = [
    path('role/add/', RoleAddView.as_view(), name='role-add'),
]
