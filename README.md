Django
======

This repository will be removed as soon as the project is finished.. it is meant as a working environment for the EPITA 2014 RIP project. 

Settings
--------

To make this project work you need to do the following \n
1. Install python 2.7 on your computer
2. Install pip
3. Install virtualenv
4. Create a virtual environment
5. Start a project with the code "django-admin.py startproject choose-a-name"
6. Go into this new folder and delete all files created
7. start git, and pull everything from this repository
8. write: "pip install -r requirements.txt" to install all the needed external apps


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

Bootstrap and JQuery is installed as apps, because it makes it easier to allow their usage in all parts of the websites. \n

In all apps there is a test directory, all test made should be put into this directory and be named "test_" + name of the 
part of the program it test (model, view etc.). \n

For specific information about django, most can be found on djangos website: 
https://docs.djangoproject.com/en/1.6/contents/

Commands that are good to know
-------------------------------

1. django-admin.py startproject name-of-project
2. python manage.py startapp name-of-app
3. python manage.py syncdb (To sync the database)
4. python manage.py test (to run standard django tests)
6. python manage.py test --settings=leapkit.settings.testing (to make sure to use the settings defined in testing.py)
6. coverage run manage.py test (better way to run tests)
7. coverage report (To create a report showing how much of the program your tests covers)
8. coverage html (to create a html sites that show which parts of your code is tested and which parts that still need to be tests)
