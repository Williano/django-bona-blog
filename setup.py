#!/usr/bin/env python

import os
from codecs import open
from setuptools import setup
import metadata

app_name = metadata.name
version = metadata.version
this_dir = os.path.dirname(os.path.abspath(__file__))


def read(filename):
    with open(filename, encoding='utf-8') as fo:
        return fo.read()


long_description = read('README.rst') + '\n\n' + \
                   read(os.path.join(this_dir, 'Changelog.rst'))

setup(
    name='django-{0}'.format(app_name),
    version=version,
    packages=['tinymce'],
    include_package_data=True,
    author='Roman Miroshnychenko (fork author)',
    author_email='roman1972@gmail.com',
    description='A Django application that provides '
                'a fully functional TinyMCE 4 editor widget for models and forms.',
    long_description=long_description,
    license='MIT License',
    keywords='django wysiwyg editor widget tinymce',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url='https://github.com/romanvm/django-tinymce4-lite',
    install_requires=[
        'Django>=1.11',
        'jsmin',
    ],
    zip_safe=False
)
