Firsts steps
============

Idea\ :sup:`X` is developed in python 3 with Django, so you need to prepare your development environment. For this, we considered that you already have it in your machine. To confirm, please, use the following command in your terminal.

.. code::

  $ python3 --version
  Python 3.6.5

After, clone the project in your computer:

.. code::

  $ git clone https://github.com/filhocf/ideax.git

Now, you need create your python environment and load it, using the package virtualenv. In a linux env, can be something like this:

.. code::

  $ sudo apt install python3-virtualenv
  $ python3 -m venv ~/.env
  $ . ~/.env/bin/activate

By end, to install the required packages:

.. code::

  $ cd ~/ideax
  $ pip install -r requerements.txt


Loading the system
------------------
With the system installed, you need create a .env file into root directory, copying the file env.example and changing what is necessary.

In .env file, you need to add a secret key. To generate it, type the following commands in prompt and, at end, will generate a long string. Copy it and past into .env file, for secret_key variable.

.. code::

    $ python
    >>> from django.utils.crypto import get_random_string
    >>> chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    >>> get_random_string(50, chars)
    

After, you need to create/populate the database, create a user and at end run the server in development mode.

.. code::

  $ ./manage.py migrate
  $ ./manage.py createsuperuser
  $ ./manage.py runserver

Extra settings
--------------
If you want to work with LDAP or MySQL, you need to install some aditional development packages in your system. In a linux box:

.. code::

  $ sudo apt install gcc libpython3.5-dev         # minimal packages to build python libs
  $ sudo apt install libldap2-dev libsasl2-dev    # packages to work with LDAP
  $ pip install -r pyldap django-auth-ldap
  $ sudo apt install libmariadbclient-dev         # package to work with MySQL
  $ pip install -r mysqlclient
  $ sudo apt install gettext                      # package to work with localization (translation)
