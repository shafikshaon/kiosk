from django.urls import path

from accounts.views import AdminLoginView

__author__ = "Shafikur Rahman"

app_label = 'accounts'
urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin-login')
]
