import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='django-bona-blog',
    version='1.1.4',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    author='William Kpabitey Kwabla (fork author)',
    author_email='paawilly17@gmail.com',
    description='A Django blog app with features of a standard blogging platform.',
    long_description=README,
    long_description_content_type="text/markdown",
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
        'six',
        'Pillow',
        'django-ckeditor',
        'django-filter',
        'django-taggit',
        'djangorestframework',
        'django-crispy-forms',
    ],
    python_requires='>=3.6',
    zip_safe=False,
)
