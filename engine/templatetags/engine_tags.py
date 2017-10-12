from django import forms
from django import template

register = template.Library()


@register.filter(name='upper')
def upper(value):
    return value.upper()


@register.filter(name='date_sort')
def date_sort(instance):
    return instance.order_by("-id")


@register.inclusion_tag('widgets/breadcrumb.html')
def breadcrumb(steps):
    return dict(steps=steps)


@register.inclusion_tag('widgets/menubar.html')
def menubar(project=None, edit_project=False, edit_data=False, data=None,
            create_project=False, upload_data=False):

    return dict(
        project=project, edit_project=edit_project, create_project=create_project,
        data=data, edit_data=edit_data, upload_data=upload_data
    )


@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, forms.BooleanField)
