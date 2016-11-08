from django.contrib import admin
from dj_web_rich_object import models


class WebRichObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'get_link', 'site_name', 'type')
    list_filter = ('type', 'create_at', 'updated_at')
    date_hierarchy = 'updated_at'
    ordering = ('-updated_at',)


admin.site.register(models.WebRichObject, WebRichObjectAdmin)
