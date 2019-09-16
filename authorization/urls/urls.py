from django.urls import path

from authorization.views.role import RoleAddView, RoleListView, RoleDetailView, RoleChangeView

__author__ = "Shafikur Rahman"

urlpatterns = [
    path('role/add/', RoleAddView.as_view(), name='role-add'),
    path('role/list/', RoleListView.as_view(), name='role-list'),
    path('role/view/<pk>/', RoleDetailView.as_view(), name='role-view'),
    path('role/change/<pk>/', RoleChangeView.as_view(), name='role-change'),
]
