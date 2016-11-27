from __future__ import unicode_literals

try:
    from urllib.parse import urlparse, parse_qs, quote
except ImportError:
    from urlparse import urlparse, parse_qs
    from urllib2 import quote

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response

import web_rich_object

EMBED_YOUTUBE_TEMPLATE = 'https://www.youtube.com/embed/%(id)s'
EMBED_FACEBOOK_TEMPLATE = 'https://www.facebook.com/plugins/video.php?href=%(id)s&show_text=0&width=560'


class WebRichObjectManager(models.Manager):
    def create_from_url(self, url=None):
        wro = web_rich_object.WebRichObject(url)
        instance = self.create(title=wro.title,
                               type=wro.type,
                               image=wro.image,
                               url=wro.url,
                               base_url=url,
                               site_name=wro.site_name,
                               description=wro.description)
        return instance

    def create_or_update_from_url(self, url):
        if self.filter(base_url=url).exists():
            return self.filter(base_url=url).first()
        else:
            return self.create_from_url(url=url)


@python_2_unicode_compatible
class WebRichObject(models.Model):
    title = models.CharField(max_length=300, verbose_name=_("title"))
    type = models.CharField(max_length=30, verbose_name=_("type"))
    image = models.URLField(null=True, blank=True, verbose_name=_("image"))
    url = models.TextField(max_length=500, verbose_name=_("URL"))

    base_url = models.TextField(max_length=500, verbose_name=_("Base URL"))

    site_name = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("site name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_valid = models.BooleanField(default=True)

    objects = WebRichObjectManager()

    class Meta:
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

    def get_widget(self):
        return render_to_response(self.template_name, {'obj': self}).getvalue()

    def get_embed_url(self):
        if 'youtube' in self.url:
            return self.get_embed_youtube()
        elif 'facebook' in self.url:
            return self.get_embed_facebook()
        else:
            raise NotImplementedError("")

    def get_embed_youtube(self):
        parsed_url = urlparse(self.url)
        video_id = parse_qs(parsed_url.query).get('v')[0]
        return EMBED_YOUTUBE_TEMPLATE % {'id': video_id}

    def get_embed_facebook(self):
        video_id = quote(self.url)
        return EMBED_FACEBOOK_TEMPLATE % {'id': video_id}
