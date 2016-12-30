"""Setup script of dj_web_rich_object"""
from setuptools import setup, find_packages
import dj_web_rich_object


def read(filename):
    with open(filename) as fd:
        return fd.read()

setup(
    name='django-web-rich-object',
    version=dj_web_rich_object.__version__,
    description=dj_web_rich_object.__doc__,
    long_description=read('README.rst'),
    keywords=dj_web_rich_object.__keywords__,
    author=dj_web_rich_object.__author__,
    author_email=dj_web_rich_object.__email__,
    url=dj_web_rich_object.__url__,
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=dj_web_rich_object.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=read('requirements.txt').splitlines(),
)
