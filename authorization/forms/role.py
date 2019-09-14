from django.contrib.contenttypes.models import ContentType

__author__ = 'Shafikur Rahman'

from django import forms

from authorization.models import Role, RolePermission


class RoleForm(forms.ModelForm):
    skipped_content_type_ids = []

    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Role name', 'autocomplete': 'off'}
        ),
        required=True
    )
    if len(skipped_content_type_ids) == 0:
        skipped_content_type_ids = list(ContentType.objects.filter(
            model__in=['contenttype', 'session']
        ).values_list(
            'pk', flat=True
        ))

    permissions = forms.ModelMultipleChoiceField(
        queryset=RolePermission.objects.exclude(
            content_type_id__in=skipped_content_type_ids
        ).select_related('content_type'),
        to_field_name='pk',
        label='Permissions',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control permissions',
                'multiple': 'multiple',
                'id': 'permission-select',
            }
        ),
        required=False
    )

    class Meta:
        model = Role
        fields = ('name', 'permissions')
