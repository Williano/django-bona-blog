<p align="center"> 
<img src="https://user-images.githubusercontent.com/19711677/86859686-cd429700-c088-11ea-8f60-9c7879d7fcc9.PNG">
</p>

<h1 align="center">django-bona-blog</h1>

<p align="center"> 
A Django blog app with features of a standard blogging platform.
</p>

<p align="center">
        <a href="https://pypi.org/project/django-bona-blog/"><img src="https://badge.fury.io/py/django-bona-blog.svg" alt="PyPI version" height="18"></a>
</p>


## Table of contents
* [General info](#general-info)
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
![Screenshot_2020-06-26 BONA Test Article](https://user-images.githubusercontent.com/19711677/85830620-854f7600-b752-11ea-8386-f618535cf97d.jpg)
 


## Features

* [Mobile App Version](https://github.com/Williano/Bona-Blog-Mobile)
* Dashboard for Authors
* WYSIWYG Editor
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
* TinyMCE 5
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

##### b. Add ```django_filters, tinmyce, taggit``` and ```rest_framework``` to your ```INSTALLED_APPS``` in ```settings.py```:
```
    INSTALLED_APPS = (
        ...
            'django_filters',
            'rest_framework',
            'taggit',
            'tinymce',
    )
```


##### c. Add  ```blog``` to ```INSTALLED_APPS``` in ```settings.py``` for your Django project:

```
    INSTALLED_APPS = (
        ...
        'blog.apps.BlogConfig',
    )
```

##### d. Add ``blog.urls, tinmyce.urls and api.urls`` to ``urls.py`` of your project:

```
    urlpatterns = [
      ...
      path('tinymce/', include('tinymce.urls')),
      path('blog/', include('blog.urls')),
      path('api/v1/article/', include('blog.api.v1.routers.routers')), 
  ]
```

##### e. Add configuration to serve static files in development to  ```urls.py``` of your project:

```
  
     from django.conf import settings
    
 
     if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
```

##### f. Create blog database tables
 ```
    $ python manage.py migrate blog
 ```
 
 ##### g. Add ```dashboard``` configuration to your project ```settings.py```:
 
 ```
    # Account Settings
      LOGIN_URL = '/account/login/'
      LOGIN_REDIRECT_URL = '/author/dashboard/'
      LOGOUT_REDIRECT_URL = '/account/logout/'
 ```
 
 ##### h. Add ```email configuration``` for ```account signup and password reset```
 
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
