from nui.decorators import register
from django.contrib.admin.filters import (
    AllValuesFieldListFilter, BooleanFieldListFilter, ChoicesFieldListFilter,
    DateFieldListFilter, EmptyFieldListFilter, FieldListFilter, ListFilter,
    RelatedFieldListFilter, RelatedOnlyFieldListFilter, SimpleListFilter,
)
from nui.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, StackedInline, TabularInline,
)
from nui.sites import NuiAdminSite, site
# from django.contrib.admin.sites import site

from django.utils.module_loading import autodiscover_modules

__all__ = [
    "register", "ModelAdmin", "HORIZONTAL", "VERTICAL", "StackedInline",
    "TabularInline", "NuiAdminSite", "site", "ListFilter", "SimpleListFilter",
    "FieldListFilter", "BooleanFieldListFilter", "RelatedFieldListFilter",
    "ChoicesFieldListFilter", "DateFieldListFilter",
    "AllValuesFieldListFilter", "EmptyFieldListFilter",
    "RelatedOnlyFieldListFilter", "autodiscover",
]


def autodiscover():
    autodiscover_modules('nui', register_to=site)


default_app_config = 'nui.apps.NuiAdminConfig'
