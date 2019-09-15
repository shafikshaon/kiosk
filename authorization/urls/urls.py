from django.urls import path

from authorization.views.role import RoleAddView, RoleListView

__author__ = "Shafikur Rahman"

urlpatterns = [
    path('role/add/', RoleAddView.as_view(), name='role-add'),
    path('role/list/', RoleListView.as_view(), name='role-list'),
]
