# Project Idea X

The goal of this project is to make a simple innovation system, receiving suggestions from general users and giving a way to select/promote this ideas inside the company.

More informations, read the docs in ```docs``` directory.

# FAQ

* **Why "Idea X"?**

   Because you can have a idea that is the X that will be the difference, or because your idea is 10! (X from roman numbers), or yet your idea elevated to X

# Mac Development

* Install python 3 (if not available):

`brew install python3` or `apt install python3`

* Install virtualenv

`sudo pip3 install virtualenv`

`virtualenv -p python3 ~/Dev/ideax`

* Install IdeaX dependencies:

`pip3 install -r requirements.txt`

* Activate virtualenv

`source ~/Dev/ideax/bin/activate`

* Start server:

`./manage.py runserver 0.0.0.0:8080`

* Install gettext if not installed:

`brew install gettext`

* Create symbolic links or add a new entry in PATH variable:

`brew link gettext --force`

* Build messages:

`./manage.py compilemessages`

* Updating messages:

`django-admin makemessages -l en`