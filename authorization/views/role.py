from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from authorization.forms.role import RoleForm
from authorization.models import Role
from gist.mixins.ListViewMixin import ListViewMixin

__author__ = 'Shafikur Rahman'


class RoleAddView(LoginRequiredMixin, CreateView):
    template_name = 'admin/authorization/role/add.html'
    form_class = RoleForm
    login_url = settings.ADMIN_LOGIN_REDIRECT_URL

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
        return HttpResponseRedirect(reverse('role-list'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class RoleListView(LoginRequiredMixin, ListViewMixin):
    template_name = 'admin/authorization/role/list.html'
    model = Role
    paginate_by = 10
    context_object_name = 'objects_list'

    def get_context_data(self, **kwargs):
        context = super(RoleListView, self).get_context_data(**kwargs)
        context['title'] = 'Role - List'
        context['page_headline'] = 'Role(s)'
        context['total_count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        object_list = super(RoleListView, self).get_queryset()
        search = self.request.GET.get('search1', None)
        if search:
            object_list = object_list.filter(name__icontains=search)
        return object_list.filter(is_delete=False).values(
            'pk', 'name', 'add_by__username', 'is_delete', 'add_at'
        ).order_by('-pk')


class RoleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'admin/authorization/role/detail.html'
    model = Role
    login_url = settings.ADMIN_LOGIN_REDIRECT_URL

    def get_context_data(self, **kwargs):
        context = super(RoleDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Role - Details'
        context['page_headline'] = context['object'].name
        context['permissions'] = context['object'].permissions.values('name')
        return context

    def get_queryset(self):
        queryset = super(RoleDetailView, self).get_queryset()
        return queryset.select_related('add_by', 'change_by')


class RoleChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'admin/authorization/role/change.html'
    model = Role
    form_class = RoleForm
    login_url = settings.ADMIN_LOGIN_REDIRECT_URL

    def get_context_data(self, **kwargs):
        context = super(RoleChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Role - Update'
        context['page_headline'] = context['object'].name
        return context

    def form_valid(self, form):
        role = form.save(commit=False)
        role.change_by = self.request.user
        role.save()
        form.save_m2m()
        messages.success(self.request, 'Role updated successfully.')
        return HttpResponseRedirect(reverse('role-list'))


class RoleDelete(LoginRequiredMixin, DeleteView):
    template_name = 'admin/authorization/role/role_confirm_delete.html'
    model = Role
    success_url = reverse_lazy('role-list')

    def get_context_data(self, **kwargs):
        context = super(RoleDelete, self).get_context_data(**kwargs)
        context['title'] = 'Role | Delete'
        context['page_headline'] = context['object'].name
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('role-list'))
        else:
            role = self.get_object()
            role.delete_by = self.request.user
            role.delete_at = timezone.now()
            role.is_delete = True
            # Todo: This will removed. Problem is role exists in parent Group model
            Group.objects.all().delete()
            role.save()
            messages.error(self.request, 'Role deleted successfully.')
            return HttpResponseRedirect(reverse('role-list'))
