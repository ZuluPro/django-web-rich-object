from django import forms
from django.contrib.admin import widgets as admin_widgets
from dj_web_rich_object import models


class WebRichObjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.WebRichObject
        exclude = ()
        widgets = {
            'url': admin_widgets.AdminURLFieldWidget(),
            'base_url': admin_widgets.AdminURLFieldWidget()
        }


class WebRichObjectAdminAddForm(forms.ModelForm):
    class Meta(WebRichObjectAdminForm.Meta):
        fields = ('url',)
