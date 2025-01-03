from django.contrib import admin

from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.

app_models = apps.get_app_config('home').get_models()
for model in app_models:
    try:    

        admin.site.register(model)
        admin.site.register(Permission)

    except Exception:
        pass
