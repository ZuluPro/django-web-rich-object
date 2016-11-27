from django.contrib import admin
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _
from django.contrib import messages
from dj_web_rich_object import models
from dj_web_rich_object.admin import forms


class WebRichObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'get_link', 'site_name', 'type')
    list_filter = ('type', 'create_at', 'updated_at')
    date_hierarchy = 'updated_at'
    ordering = ('-updated_at',)
    form = forms.WebRichObjectAdminForm
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                ('title', 'type', 'site_name'),
                'description',
                ('url', 'base_url'),
            )
        }),
    )

    add_form = forms.WebRichObjectAdminAddForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('url',)
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return self.add_form
        return super(WebRichObjectAdmin, self).get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return self.add_fieldsets
        return super(WebRichObjectAdmin, self).get_fieldsets(request, obj)

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'GET':
            return super(WebRichObjectAdmin, self).add_view(request, form_url, extra_context)
        try:
            wro = models.WebRichObject.objects.create_or_update_from_url(request.POST['url'])
            return redirect("/admin/dj_web_rich_object/webrichobject/%s" % wro.id)
        except Exception as err:
            msg = 'Error: %s' % (err.message or str(err.args))
            self.message_user(request, msg, messages.ERROR)
            return redirect("/admin/dj_web_rich_object/webrichobject/add/")
