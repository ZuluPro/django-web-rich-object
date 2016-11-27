from django.contrib import admin
from dj_web_rich_object import models
from dj_web_rich_object.admin import modeladmins


admin.site.register(models.WebRichObject, modeladmins.WebRichObjectAdmin)
