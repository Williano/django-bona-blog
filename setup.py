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
    author='William Kpabitey Kwabla (fork author)',
    author_email='paawilly17@gmail.com',
    description='A Django blog app with a number of features needed for a standard blog platform. '
    long_description=long_description,
    license='MIT License',
    keywords='django-blogging django django-app django-blog-app django-blog ',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url='https://github.com/Williano/django-bona-blog',
    install_requires=[
        'Django>=2.2',
        'Pillow',
        'django-tinymce4-lite',
        'django-filter',
        'django-taggit',
        'djangorestframework',
    ],
    python_requires='>=3.5',
    zip_safe=False
)
