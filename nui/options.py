from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.options import BaseModelAdmin, ModelAdmin, InlineModelAdmin, StackedInline, TabularInline
from django.db import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from functools import update_wrapper

from django.views.generic import RedirectView

IS_POPUP_VAR = '_popup'
TO_FIELD_VAR = '_to_field'

IS_SELECTED = 'is_selected'
IS_SELECTED_LABEL_CH = '全选'
IS_SELECTED_LABEL_EN = 'selected all'
TD_CLASS = 'custom-tbody-td-background-color-info'
DEFAULT_SELECTED_ITEM_CH = {
    'Key': IS_SELECTED,
    'Label': IS_SELECTED_LABEL_CH,
    'Class': "text-center text-info",
    'StickyColumn': True,
    'Fixed': "left",
    'TdClass': "custom-tbody-td-background-color-info",
}

DEFAULT_SELECTED_ITEM_EN = {
    'Key': IS_SELECTED,
    'Label': IS_SELECTED_LABEL_EN,
    'Class': "text-center text-info",
    'StickyColumn': True,
    'Fixed': "left",
    'TdClass': "custom-tbody-td-background-color-info",
}

HORIZONTAL, VERTICAL = 1, 2


def get_content_type_for_model(obj):
    # Since this module gets imported in the application's root package,
    # it cannot import models from other applications at the module level.
    from django.contrib.contenttypes.models import ContentType
    return ContentType.objects.get_for_model(obj, for_concrete_model=False)


def get_ul_class(radio_style):
    return 'radiolist' if radio_style == VERTICAL else 'radiolist inline'


class IncorrectLookupParameters(Exception):
    pass


FORMFIELD_FOR_DBFIELD_DEFAULTS = {
    models.DateTimeField: {
        'form_class': forms.SplitDateTimeField,
        'widget': widgets.AdminSplitDateTime
    },
    models.DateField: {'widget': widgets.AdminDateWidget},
    models.TimeField: {'widget': widgets.AdminTimeWidget},
    models.TextField: {'widget': widgets.AdminTextareaWidget},
    models.URLField: {'widget': widgets.AdminURLFieldWidget},
    models.IntegerField: {'widget': widgets.AdminIntegerFieldWidget},
    models.BigIntegerField: {'widget': widgets.AdminBigIntegerFieldWidget},
    models.CharField: {'widget': widgets.AdminTextInputWidget},
    models.ImageField: {'widget': widgets.AdminFileWidget},
    models.FileField: {'widget': widgets.AdminFileWidget},
    models.EmailField: {'widget': widgets.AdminEmailInputWidget},
    models.UUIDField: {'widget': widgets.AdminUUIDInputWidget},
}

csrf_protect_m = method_decorator(csrf_protect)


class NuiBaseModelAdmin(BaseModelAdmin):
    pass


class NuiModelAdmin(ModelAdmin):
    list_per_page = 10
    list_max_show_all = 50
    list_display_fields = []

    def __init__(self, model, admin_site):
        super(NuiModelAdmin, self).__init__(model, admin_site)
        self.settings = None
        self._get_current_settings()
        self._list_display_fields_action()

    def _get_current_settings(self):
        self.settings = settings._wrapped

    def _list_display_fields_action(self):
        has_key = False
        for dispaly_field in self.list_display_fields:
            if dispaly_field.get("key") == IS_SELECTED and dispaly_field.get("TdClass") is None:
                dispaly_field.update({'TdClass': TD_CLASS})
                has_key = True
            if dispaly_field.get("key") == IS_SELECTED and self.settings.LANGUAGE_CODE == 'zh-Hans':
                dispaly_field.update({'label': IS_SELECTED_LABEL_CH})
                has_key = True
            if dispaly_field.get("key") == IS_SELECTED and self.settings.LANGUAGE_CODE != 'zh-Hans':
                dispaly_field.update({'label': IS_SELECTED_LABEL_EN})
                has_key = True
            if dispaly_field.get("key") == IS_SELECTED:
                break
        if not has_key and self.settings.LANGUAGE_CODE == 'zh-Hans':
            self.list_display_fields.insert(0, DEFAULT_SELECTED_ITEM_CH)

        if not has_key and self.settings.LANGUAGE_CODE != 'zh-Hans':
            self.list_display_fields.insert(0, DEFAULT_SELECTED_ITEM_EN)

    def nui_get_model_field(self, cl):

        res = {
            # 'fields': model_obj._meta.fields
        }
        return res

    def nui_get_changelist_instance(self, request):
        cl = self.get_changelist_instance(request)
        x = self.nui_get_model_field(cl)
        res = {
            'can_show_all': cl.can_show_all,
            'clear_all_filters_qs': cl.clear_all_filters_qs,
            'date_hierarchy': cl.date_hierarchy,
            # 'filter_specs': cl.filter_specs,
            'full_result_count': cl.full_result_count,
            'has_active_filters': cl.has_active_filters,
            'has_filters': cl.has_filters,
            'is_popup': cl.is_popup,
            'list_display': cl.list_display,
            'list_display_links': cl.list_display_links,
            'list_per_page': cl.list_per_page,
            'list_editable': cl.list_editable,
            'list_filter': cl.list_filter,
            'list_max_show_all': cl.list_max_show_all,
            'list_select_related': cl.list_select_related,
            'multi_page': cl.multi_page,
            'page_num': cl.page_num,
            'pk_attname': cl.pk_attname,
            'preserved_filters': cl.preserved_filters,
            'query': cl.query,
            'result_count': cl.result_count,
            'search_fields': cl.search_fields,
            'show_admin_actions': cl.show_admin_actions,
            'show_all': cl.show_all,
            'show_full_result_count': cl.show_full_result_count,
            'sortable_by': cl.sortable_by,
            'title': cl.title,
            'to_field': cl.to_field,
            'opts': {
                'verbose_name': cl.opts.verbose_name,
                'verbose_name_plural': cl.opts.verbose_name_plural,
                'verbose_name_raw': cl.opts.verbose_name_raw,
                'original_attrs': cl.opts.original_attrs,
                'model_name': cl.opts.model_name,
                'object_name': cl.opts.object_name
            }
        }
        return cl, res


class NuiInlineModelAdmin(InlineModelAdmin):
    pass


class NuiStackedInline(StackedInline):
    pass


class NuiTabularInline(TabularInline):
    pass
