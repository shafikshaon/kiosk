from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url

from accounts.forms.login import LoginForm

__author__ = 'Shafikur Rahman'


class AdminLoginView(LoginView):
    template_name = "admin/accounts/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return resolve_url(settings.ADMIN_LOGIN_REDIRECT_URL)
