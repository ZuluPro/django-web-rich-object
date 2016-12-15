from django.test import TestCase
from web_rich_object import functional_tests as utils
from dj_web_rich_object import models


def gen_test(url, wro_attrs):
    def func(self):
        wro = models.WebRichObject.objects.create_from_url(url)
        # Test attrs
        attrs = {k: getattr(wro, k) for k, v in wro_attrs.iteritems() if hasattr(wro, k)}
        expected_attrs = {k: v for k, v in wro_attrs.iteritems() if hasattr(wro, k)}
        self.assertEqual(attrs, expected_attrs)
        # Test widget
        widget = wro.get_widget()
    return func


class MetaFunctionalTest(type):
    def __new__(mcls, name, bases, attrs):
        for url, wro_attrs in utils.TEST_URLS:
            func_name = 'test_' + utils.NOT_ALPHA_REG.sub('_', url)
            func_name = utils.UNDERSCORE_REG.sub('_', func_name)[:100]
            func = gen_test(url, wro_attrs)
            attrs[func_name] = func
        return type.__new__(mcls, name, bases, attrs)


class FunctionalTest(TestCase):
    __metaclass__ = MetaFunctionalTest
    maxDiff = None
