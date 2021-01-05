from _weakrefset import WeakSet
from functools import update_wrapper

from django.apps import apps
# from django.contrib.admin import actions
from django.contrib.admin import actions
from django.contrib.admin.sites import AdminSite
from django.template.response import TemplateResponse
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy
from django.views.decorators.cache import never_cache
from django.conf import settings
import collections
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError

all_sites = WeakSet()

NUI_SIDEBAR_PROPS = {
    'NUI_EXACT': True,
    'NUI_SIDE_MINI': True,
    'NUI_CONTAINER_VARIANT': "darkPrimary",
    'NUI_CONTAINER_HOVER': True,
    'NUI_CONTAINER_ELEVATION': 'xl',
    'NUI_BRAND_SIZE': None,
    'NUI_BRAND_ELEVATION': 'xl',
    'NUI_BRAND_TO': '/',
    'NUI_BRAND_IMG_SRC': 'http://gin-admin.nejinn.com/img/NLYLOGO.b43761e2.png',
    'NUI_BRAND_IMG_CIRCLE': True,
    'NUI_BRAND_TEXT': "Nui-Admin",
    'NUI_SCROLLBAR': True,
}

NUI_AUTH_ICON = 'nav-icon far nlyfont nly-icon-logo-steam'
NUI_SIDEBAR_ICON = 'nav-icon far nlyfont nly-icon-nav-tool'


class NuiAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy('Nui1 admin')

    # Text to put in each page's <h1>.
    site_header = gettext_lazy('Nui admin')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('Site administration')

    # def __init__(self, name='nui'):
    #     self._registry = {}  # model_class class -> admin_class instance
    #     self.name = name
    #     self._actions = {'delete_selected': actions.delete_selected}
    #     self._global_actions = self._actions.copy()
    #     all_sites.add(self)

    def __init__(self, name='nui'):
        super().__init__(name)
        self.settings = None
        self._get_current_settings()

    def _get_current_settings(self):
        self.settings = settings._wrapped

    def get_side_props(self, request):
        side_props = collections.OrderedDict()
        models_register_dict = {m._meta.object_name: m_a for m, m_a in self._registry.items()}
        for side_prop in NUI_SIDEBAR_PROPS:
            prop_key = "-".join(side_prop.lower().split("_")[1:])
            prop_value = getattr(self.settings, side_prop, NUI_SIDEBAR_PROPS[side_prop])
            side_props.setdefault(prop_key, prop_value)

        app_list = self.get_app_list(request)
        app_sidebar_list = [
            {
                '_type': "nly-sidebar-nav",
                '_class': "mt-2",
                'dataGroup': "nui-admin",
                '_key': "nui",
                'exact': True,
                "child-indent": True,
                '_children': []
            }
        ]

        for app_list_item in app_list:
            if app_list_item['has_module_perms']:
                nui_default_icon = getattr(self.settings, 'NUI_SIDEBAR_ICON', NUI_SIDEBAR_ICON)
                app_config = apps.app_configs.get(app_list_item.get('app_label'))
                nui_current_app_icon = getattr(app_config, 'icon', nui_default_icon)
                if app_list_item.get('app_label') == 'auth':
                    nui_current_app_icon = getattr(app_config, 'NUI_AUTH_ICON', NUI_AUTH_ICON)
                sidebar_tree = {
                    '_type': "nly-sidebar-nav-tree",
                    'target': app_list_item['app_label'],
                    'icon': nui_current_app_icon,
                    'text': app_list_item['name'],
                    'dataGroup': "nui",
                    '_key': app_list_item['app_label'],
                    'exact': True,
                    '_children': []
                }
                app_sidebar_list_models = app_list_item.get("models")
                if app_sidebar_list_models:
                    for app_sidebar_list_model in app_sidebar_list_models:
                        model_register = models_register_dict[app_sidebar_list_model['object_name']]
                        model_icon = getattr(model_register, 'icon', nui_default_icon)
                        sidebar_item = {
                            '_type': "nly-sidebar-nav-item",
                            '_name': app_sidebar_list_model['name'],
                            'icon': model_icon,
                            'exact': True,
                            'exactActiveClass': "active",
                            'dataGroup': app_list_item['app_label'],
                            '_key': app_sidebar_list_model['name'],
                            'to': app_sidebar_list_model['admin_url']
                        }
                        sidebar_tree['_children'].append(
                            sidebar_item
                        )

                app_sidebar_list[0]['_children'].append(sidebar_tree)

        side_props.setdefault('sidebar-list', app_sidebar_list)
        return side_props

    def get_urls(self):
        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.contenttypes.views imports ContentType.
        from django.contrib.contenttypes import views as contenttype_views
        from django.urls import include, path, re_path
        from nui.views import UserLoginAPIView, UserSidebarAPIView

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        # Admin-site-wide views.
        urlpatterns = [
            path('login/', UserLoginAPIView.as_view()),
            path('sidebar/', UserSidebarAPIView.as_view()),
        ]

        # Add in each model's views, and create a list of valid URLS for the
        # app_index
        valid_app_labels = []
        for model, model_admin in self._registry.items():
            urlpatterns += [
                path('%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]
            if model._meta.app_label not in valid_app_labels:
                valid_app_labels.append(model._meta.app_label)

        # If there were ModelAdmins registered, we should have a list of app
        # labels for which we need to allow access to the app_index view,
        if valid_app_labels:
            regex = r'^(?P<app_label>' + '|'.join(valid_app_labels) + ')/$'
            urlpatterns += [
                re_path(regex, wrap(self.app_index), name='app_list'),
            ]
        return urlpatterns


class DefaultAdminSite(LazyObject):
    def _setup(self):
        AdminSiteClass = import_string(apps.get_app_config('nui').default_site)
        self._wrapped = AdminSiteClass()


# This global object represents the default admin site, for the common case.
# You can provide your own AdminSite using the (Simple)AdminConfig.default_site
# attribute. You can also instantiate AdminSite in your own code to create a
# custom admin site.
site = DefaultAdminSite()
