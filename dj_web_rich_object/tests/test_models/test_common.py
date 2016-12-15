from django.test import TestCase
from web_rich_object.tests import utils
from web_rich_object import api
from dj_web_rich_object import models


class WebRichObjectTest(TestCase, utils.BaseWebRichObjectTestCase):
    def test_create_from_url(self):
        base_wro = api.WebRichObject(self.url)
        wro = models.WebRichObject.objects.create_from_url(self.url)
        self.assertEqual(wro.title, base_wro.title)
        self.assertEqual(wro.url, base_wro.url)
        self.assertEqual(wro.base_url, base_wro.base_url)
        self.assertEqual(wro.site_name, base_wro.site_name)
        self.assertEqual(wro.image, base_wro.image)
        self.assertEqual(wro.type, base_wro.type)
        self.assertEqual(wro.subtype, base_wro.subtype)
        self.assertEqual(wro.description, base_wro.description)
        self.assertEqual(wro.author, base_wro.author)
    test_create_from_url.mock_attrs = {
        'return_value.read.return_value': '<html><meta property="og:title" content="foo"/></html>',
        'return_value.info.return_value.__dict__': utils.HTML_RESPONSE_INFO,
    }

    def test_create_or_update_from_url(self):
        models.WebRichObject.objects.create_from_url(self.url)
        models.WebRichObject.objects.create_or_update_from_url(self.url)
        self.assertEqual(models.WebRichObject.objects.count(), 1)
    test_create_or_update_from_url.mock_attrs = {
        'return_value.read.return_value': '',
        'return_value.info.return_value.__dict__': utils.UNKNOW_RESPONSE_INFO,
    }

    def test_get_widget(self):
        wro = models.WebRichObject.objects.create_from_url(self.url)
        widget = wro.get_widget()
        self.assertIsInstance(widget, str)
    test_get_widget.mock_attrs = {
        'return_value.read.return_value': '',
        'return_value.info.return_value.__dict__': utils.UNKNOW_RESPONSE_INFO,
    }
