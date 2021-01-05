from django.apps import AppConfig
from django.contrib.admin.checks import check_admin_app, check_dependencies
from django.core import checks
from django.utils.translation import gettext_lazy as _


class NuiSimpleAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    default_site = 'nui.sites.NuiAdminSite'
    name = 'nui'
    verbose_name = _("Administration")
    icon = 'nav-icon far nlyfont nly-icon-user-fill'

    def ready(self):
        checks.register(check_dependencies, checks.Tags.admin)
        checks.register(check_admin_app, checks.Tags.admin)


class NuiAdminConfig(NuiSimpleAdminConfig):
    """The default AppConfig for admin which does autodiscovery."""

    def ready(self):
        super().ready()
        self.module.autodiscover()
