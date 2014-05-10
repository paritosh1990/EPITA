Django
======

This repository will be removed as soon as the project is finished.. it is meant as a working environment for the EPITA 2014 RIP project. 

Getting started
--------

To get started with this project work you need to do the following

1. Install **python 2.7** on your computer
2. Install **pip**
3. Install **virtualenv**
4. Create a virtual environment
5. Start a project with the code: **django-admin.py startproject choose-a-name**
6. Go into this new folder and delete the folder with the name you just chose
7. Start git, and pull everything from this repository
8. Write: **pip install -r requirements.txt** to install all the needed external apps

The file structure inside your virtual environment should look like this

<pre>
+-- bin
+-- include
+-- leapkit
|   +-- admin
|	|   +-- static
|	|   +-- templates
|	|   +-- tests
|   +-- companies
|	|   +-- static
|	|   +-- templates
|	|   +-- tests
|   +-- leapkit
|	|   +-- static
|	|   +-- templates
|	|   +-- tests
|   +-- students
|	|   +-- static
|	|   +-- templates
|	|   +-- tests
|   +-- .gitignore
|   +-- manage.py
|   +-- README.md
|   +-- requirements.txt
+-- lib
</pre>

Database
--------
The database is currently SQLlite since this makes it easier to work on on multiple computers

Name           |Value         
:---           |:---:
User name:     |test           
Email: 		   |test@test.dk   
Password:	   |test           


Important Information
---------------------

Bootstrap and JQuery is installed as apps, because it makes it easier to allow their usage in all parts of the websites.

In all apps there is a test directory, all test made should be put into this directory and be named "test_" + name of the 
part of the program it test (e.g **test_model**, **test_view**).

All apps contain a folder called **static**. This is for static files such as **CSS**, **JavaScript**, **Images** etc. However, they need to be placed inside another folder with the same name as the app itself. I have added such a folder already. If custom CSS is needed it would then have to be placed inside a folder called **css**. 

All **HTML** files will need to be put inside the **templates folder**, also included in all apps. If any of the html folders are used as templates, they should be included in a folder called **_layouts** inside **templates**. 

For specific information about django, most can be found on djangos website: 
https://docs.djangoproject.com/en/1.6/contents

Selenium is installed and can be used for testing, for more information and tutorials, here are some links:

1. http://lincolnloop.com/blog/introduction-django-selenium-testing/
2. http://blog.wercker.com/2013/11/28/django-selenium.html
3. http://www.realpython.com/blog/python/django-1-6-test-driven-development/

Commands that are good to know
-------------------------------

1. **django-admin.py startproject name-of-project**
2. **python manage.py startapp name-of-app**
3. **python manage.py syncdb** (To sync the database)
4. **python manage.py test** (to run standard django tests)
6. **python manage.py test --settings=leapkit.settings.testing** (to make sure to use the settings defined in testing.py)
6. **coverage run manage.py test** (better way to run tests)
7. **coverage report** (To create a report showing how much of the program your tests covers)
8. **coverage html** (to create a html site showing which parts of your code is tested and which parts that still need to be tests)
