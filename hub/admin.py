from django.contrib import admin
from .models import HubDoggyModel, PhotoDoggyModel


admin.site.register(PhotoDoggyModel)


@admin.register(HubDoggyModel)
class AdminHubDoggy(admin.ModelAdmin):
    readonly_fields = ('slug',)
