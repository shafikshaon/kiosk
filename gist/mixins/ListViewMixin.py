from django.views.generic import ListView

__author__ = "Shafikur Rahman"


class ListViewMixin(ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListViewMixin, self).get_context_data(object_list=None, **kwargs)
        context['order_by_columns'] = self.model.get_order_by_columns
        context['searchable_columns'] = self.model.get_searchable_columns
        return context
