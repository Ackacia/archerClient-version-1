from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig as BaseAdminConfig


class Auth2FaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth2FA'


class CustomAdminConfig(BaseAdminConfig):
    default_site = "auth2FA.sites.AdminSite"
