How to install Idea\ :sup:`X`
=============================

Introduction
------------

Idea\ :sup:`X` is a Django application, so you can download it and install in a WSGI server or use a Docker image.

Installation
------------

Get Idea\ :sup:`X`!
^^^^^^^^^^^^^^^^^^^

You can clone its repository or download its zip file.
.. code::

  $ git clone https://github.com/filhocf/ideax.git

.. code::

  $ wget https://github.com/filhocf/ideax/archive/master.zip

Install dependencies
^^^^^^^^^^^^^^^^^^^^

If you want to authenticate against a LDAP or AD server, you need to install some python packages for LDAP and its dependencies.
It and others dependencies are listed in requirements.txt file.

.. code::

  $ sudo apt install gcc libpython3.5-dev libldap2-dev libsasl2-dev
  $ pip install -r requirements.txt


Database Configuration
^^^^^^^^^^^^^^^^^^^^^^
If prefer, you can choice a database to use as backend. The most common is MySQL but others are PostgreSQL and SQLite. SQLite is native and don't requires any action to use. For others, is necessary to install the related python package to support it. After, create a database with any name you want and grant privileges to a separate database user.

Considering to use MySQL as database, use following commands:
.. code::

  $ sudo apt install libmariadbclient-dev
  $ pip install mysqlclient

And in the mysql server:

.. code:: sql

  CREATE DATABASE ideax;
  GRANT ALL PRIVILEGES ON ideax.* TO username@localhost IDENTIFIED BY 'password';
  FLUSH PRIVILEGES;

Run with Docker
---------------

You can run IdeaX with SQLLite or a database server, like MySql. For the first, run the following command, otherwise use the next instructions.
.. code::

  $ docker run -d -p 80:8000 --name ideax filhocf/ideax # run with sqlite3

For customized environment, is possible to map the .env file. For this propose, copy or rename env.example file. After to up the database server don't forget to create tables as described above.
.. code::

  $ docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=password mysql
  $ docker run -d -p 80:8000 --name ideax -v .env:/var/www/ideax/.env --link mysql:mysql filhocf/ideax
