from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist

import web_rich_object


class WebRichObjectManager(models.Manager):
    def create_from_url(self, url=None, **kwargs):
        wro = web_rich_object.WebRichObject(url)
        wro_attrs = {
            'title': wro.title,
            'site_name': wro.site_name,
            'description': wro.description,

            'type': wro.type,
            'subtype': wro.subtype,

            'image': wro.image,

            'url': wro.url,
            'base_url': wro.base_url,

            'author': wro.author,
            'created_time': wro.created_time,
            'published_time': wro.published_time,
            'modified_time': wro.modified_time,

            'video': wro.video,
            'video_width': wro.video_width,
            'video_height': wro.video_height,
        }
        wro_attrs.update(kwargs)
        instance = self.create(**wro_attrs)
        return instance

    def create_or_update_from_url(self, url, **kwargs):
        if self.filter(base_url=url).exists():
            # TODO: Update not implemented
            return self.filter(base_url=url).first()
        else:
            return self.create_from_url(url=url, **kwargs)


@python_2_unicode_compatible
class WebRichObject(models.Model):
    title = models.CharField(max_length=300, verbose_name=_("title"))
    type = models.CharField(max_length=30, verbose_name=_("type"))
    subtype = models.CharField(max_length=30, verbose_name=_("subtype"))

    url = models.TextField(max_length=500, verbose_name=_("URL"))
    base_url = models.TextField(max_length=500, verbose_name=_("Base URL"))

    image = models.URLField(null=True, blank=True, verbose_name=_("image"))

    video = models.URLField(null=True, blank=True, verbose_name=_("video"))
    video_width = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("video width"))
    video_height = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("video height"))

    site_name = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("site name"))
    description = models.TextField(null=True, blank=True, default='', verbose_name=_("description"))
    author = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name=_("author"))

    created_time = models.DateTimeField(blank=True, null=True, default=None, verbose_name=_("created time"))
    published_time = models.DateTimeField(blank=True, null=True, default=None, verbose_name=_("published time"))
    modified_time = models.DateTimeField(blank=True, null=True, default=None, verbose_name=_("modified time"))

    # Plus
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    objects = WebRichObjectManager()

    class Meta:
        app_label = 'dj_web_rich_object'
        verbose_name = _("web rich object")
        verbose_name_plural = _("web rich objects")

    def __str__(self):
        return self.title

    def get_link(self, target='_blank', text=None):
        return '<a href="%(url)s" target="%(target)s">%(text)s</a>' % {
            'url': self.url,
            'target': target,
            'text': text or self.url
        }
    get_link.short_description = _('Link')
    get_link.allow_tags = True

    def get_image(self, target='_blank'):
        if not self.image:
            return ''
        return '<a href="%(url)s" target="%(target)s"><img src="%(image)s" height="40px"></a>' % {
            'url': self.image,
            'target': target,
            'image': self.image,
        }
    get_image.short_description = _('Image')
    get_image.allow_tags = True

    @property
    def template_name(self):
        return 'wro/widget_%s.html' % self.type

    def get_widget(self, **kwargs):
        context = kwargs.copy()
        context['obj'] = self
        try:
            if self.type == 'video' and self.video is None:
                raise TemplateDoesNotExist("No video provided")
            return render_to_response(self.template_name, context).getvalue()
        except TemplateDoesNotExist:
            return render_to_response('wro/widget_website.html', context).getvalue()
