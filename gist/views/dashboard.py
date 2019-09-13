from django.views.generic import TemplateView

__author__ = 'Shafikur Rahman'


class DashboardView(TemplateView):
    template_name = 'admin/gist/dashboard.html'
