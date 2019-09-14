from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from authorization.forms.role import RoleForm

__author__ = 'Shafikur Rahman'


class RoleAddView(LoginRequiredMixin, CreateView):
    template_name = 'admin/authorization/role/add.html'
    form_class = RoleForm
    login_url = 'admin/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(RoleAddView, self).get_context_data(**kwargs)
        context['title'] = 'Role - Add'
        context['page_headline'] = 'New'
        return context

    def get(self, request, *args, **kwargs):
        return super(RoleAddView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        role = form.save(commit=False)
        role.add_by = self.request.user
        role.save()
        form.save_m2m()
        messages.success(self.request, 'Role added successfully.')
        return HttpResponseRedirect(reverse('role-add'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
