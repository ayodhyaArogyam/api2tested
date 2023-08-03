from .models import HrSettings
from django.contrib import admin


@admin.register(HrSettings)
class HrSettingsAdmin(admin.ModelAdmin):
    pass
