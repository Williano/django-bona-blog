<p align="center"> 
<img src="https://user-images.githubusercontent.com/19711677/86859686-cd429700-c088-11ea-8f60-9c7879d7fcc9.PNG">
</p>


<h1 align="center">django-bona-blog</h1>

<p align="center"> 
A Django blog app with features of a standard blogging platform.
</p>



<a href="https://badge.fury.io/py/django-bona-blog"><img src="https://badge.fury.io/py/django-bona-blog.svg" alt="PyPI version" height="28"></a>
[![GitHub license](https://img.shields.io/github/license/Williano/Bona-Blog-Mobile?style=for-the-badge)](https://img.shields.io/github/license/Williano/Bona-Blog-Mobile?style=for-the-badge)
[![GitHub stars](https://img.shields.io/github/stars/Williano/django-bona-blog?style=for-the-badge)](https://img.shields.io/github/stars/Williano/django-bona-blog?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/Williano/Bona-Blog-Mobile?style=for-the-badge)](https://img.shields.io/github/forks/Williano/Bona-Blog-Mobile?style=for-the-badge)
[![GitHub issues](https://img.shields.io/github/issues/Williano/Bona-Blog-Mobile?style=for-the-badge)](https://img.shields.io/github/issues/Williano/Bona-Blog-Mobile?style=for-the-badge)


## Table of contents
* [General info](#general-info)
* [Standalone Project](#standalone-project)
* [Screenshots](#screenshots)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info
An Open-Source Django blogging app like [Medium](https://medium.com/) and [Real Python](https://realpython.com/). It has [features](#features) of a standard blogging platform.

## Standalone Project
There is a standalone version of this django package. You can get it from its [GitHub Repo](https://github.com/Williano/Bona-Blog).

## Screenshots

 Authors Dashboard Page
:-------------------------:
![Screenshot_2020-06-25 Bona Dashboard Home](https://user-images.githubusercontent.com/19711677/85830207-d4e17200-b751-11ea-9de2-0a86b5bd296a.png)

 Create Article Page
:-------------------------:
![Screenshot_2020-06-26 Bona Dashboard Create Article(2)](https://user-images.githubusercontent.com/19711677/85830197-d1e68180-b751-11ea-9a10-9653fc0c1a9d.png)


Authors Profile Details Page
:-------------------------:
![Screenshot_2020-06-25 Bona Dashboard Profile Details](https://user-images.githubusercontent.com/19711677/85830204-d317ae80-b751-11ea-86ff-c7b5683ffea5.png)


Home Page            |  List of Categories Page
:-------------------------:|:-------------------------:
![Home](https://user-images.githubusercontent.com/19711677/56363189-264fb200-61db-11e9-9bba-77a3e7f7c1de.jpg) | ![Categories List](https://user-images.githubusercontent.com/19711677/56363187-264fb200-61db-11e9-8a90-0af49eb33758.jpg)

Category Articles List Page       |  Author Articles List Page
:-------------------------:|:-------------------------:
![Category Article List](https://user-images.githubusercontent.com/19711677/56363188-264fb200-61db-11e9-8fef-fc83fb29f056.png) | ![Author Articles](https://user-images.githubusercontent.com/19711677/56363185-25b71b80-61db-11e9-9a42-2fffaa369d28.jpg)

Article Detail Page 
:-------------------------:
![Screenshot_2020-11-22 BONA Django CKEditor installation Testing](https://user-images.githubusercontent.com/19711677/99898873-a0bf9e00-2c6a-11eb-8e4a-8e24af9dce94.jpg)
 


## Features

* [Mobile App Version](https://github.com/Williano/Bona-Blog-Mobile)
* Dashboard for Authors
* WYSIWYG Editor
* Account Verification 
* Author Login
* Author Password Reset
* API for Clients
* Category List
* Category Articles List
* New Category Submission
* Related Articles
* Comments
* Articles Search
* Article Social Media Share
* Article Minute Read
* Article Number of Words
* Article Number of Views
* Article Tags
* Tag Related Articles
* Markdown Support
* Responsive on all devices
* Pagination
* Clean Code
* 90% test coverage


## Technologies
* Python 3.6
* Javascript
* Jquery 
* Ajax
* PrismJS
* Django 3
* HTML5
* CSS3 
* Bootstrap 4
* Ion Icons
* Font awesome
* CKEditor
* SQLite
* PostgreSQL

## Setup

To run this app, you will need to follow these 3 steps:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (eg. vscode, PyCharm)

  - Python 3.6 +
  
  - Django 2.2+


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

##### a. Install package with pip or pipenv

      ```
          $ pip install django-bona-blog
       
      ```
      
                   or 
      ```
          $ pipenv install django-bona-blog
       
      ```             

##### b. Add ```django_filter, ckeditor, taggit, crispy_forms``` and ```rest_framework``` to your ```INSTALLED_APPS``` in ```settings.py```:
```
    INSTALLED_APPS = (
        ...
            'django_filters',
            'rest_framework',
            'taggit',
            'ckeditor',
            'ckeditor_uploader',
            'crispy_forms',
    )
```

##### c. Add ```CKEditor Configuration``` to ```settings.py```:
```
    # CKEditor Settings
    CKEDITOR_UPLOAD_PATH = 'uploads/'
    CKEDITOR_IMAGE_BACKEND = "pillow"

    CKEDITOR_CONFIGS = {
        'default':
            {'toolbar': 'full',
             'width': 'auto',
             'extraPlugins': ','.join([
                 'codesnippet',
                 'youtube'
             ]),
             },
    }
```



##### d. Add  ```blog``` to ```INSTALLED_APPS``` in ```settings.py``` for your Django project:

```
    INSTALLED_APPS = (
        ...
        'blog.apps.BlogConfig',
    )
```

##### e. Add ``blog.urls, tinmyce.urls and api.urls`` to ``urls.py`` of your project:

```

    from django.urls import include
    

    urlpatterns = [
      ...
      path('ckeditor/', include('ckeditor_uploader.urls')),
      path('blog/', include('blog.urls')),
      path('api/v1/', include('blog.api.v1.routers.routers')), 
  ]
```

##### f. Add configuration to serve static files in development to  ```urls.py``` of your project:

```
     from django.conf.urls.static import static
     from django.conf import settings
    
 
     if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
```

##### g. Create blog database tables
 ```
    $ python manage.py migrate blog
 ```
 
 ##### h. Add ```dashboard``` configuration to your project ```settings.py```:
 
 ```
    # Account Settings
      LOGIN_URL = '/account/login/'
      LOGIN_REDIRECT_URL = '/author/dashboard/'
      LOGOUT_REDIRECT_URL = '/account/logout/'
 ```
 
 ##### i. Add ```email configuration``` for ```account signup and password reset```
 
 ```
    # Email Settings (Development)
      EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



   # Email Settings (Production)
     EMAIL_BACKEND = ''
     EMAIL_HOST = ''
     EMAIL_HOST_USER = ''
     EMAIL_HOST_PASSWORD = ""
     EMAIL_PORT = 587
     EMAIL_USE_TLS = True
 ```

 ##### j. Add ```static files configuration``` for ```serving staticfiles```
 
 ```

    
      STATICFILES_DIRS = [ os.path.join(BASE_DIR, "blog/static"),]
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
      STATICFILES_FINDERS = [
            "django.contrib.staticfiles.finders.FileSystemFinder",
            "django.contrib.staticfiles.finders.AppDirectoriesFinder",
         ]
 ```
 
  ##### k. Add ```media files configuration``` for ```serving media files```
 
 ```
        # Media files (User uploaded images)
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
 ```
 
   ##### l. Collect ```static files```
 
 ```
     $ python manage.py collectstatic
 ```
 
##### Running Tests
   ```
      $ python manage.py test blog.tests
  ```


## Status
Project is: _done_


## Contact
Created by [Williano](https://williano.github.io/) - feel free to contact me!

## License
>You can check out the full license [here](https://github.com/Williano/django-bona-blog/blob/master/LICENSE)

This project is licensed under the terms of the **MIT** license.

## Contributing

1. Fork it (<https://github.com/Williano/django-bona-blog.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
