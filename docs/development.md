# Firsts steps

IdeaX is developed in python3 with Django, so you need to prepare your development environment. For this, we considered that you already have it in your machine. To confirm, please, use the following command in your terminal.

```
$ python3 --version
Python 3.6.5
```
After, clone the project in your computer:
```
$ git clone https://github.com/filhocf/ideax.git
```

Now, you need create your python environment and load it, using the package virtualenv. In a linux env, can be something like this:
```
$ sudo apt install python-virtualenv
$ python3 -m venv ~/.env
$ . ~/.env/bin/activate
```

By end, to install the required packages:
```
$ cd ~/ideax
$ pip install -r requirements.txt
```

## Loading the system

With the system installed, you need create a .env file into root directory, copying the file env.example and changing what is necessary.

After, you need to create/populate the database, create a user and at end run the server in development mode.
```
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

## Extra settings

If you want to work with LDAP or MySQL, you need to install some aditional development packages in your system. In a linux box:
```
$ sudo apt install gcc libpython3.5-dev         # minimal packages to build python libs
$ sudo apt install libldap2-dev libsasl2-dev    # packages to work with LDAP
$ pip install -r pyldap django-auth-ldap
$ sudo apt install libmariadbclient-dev         # package to work with MySQL
$ pip install -r mysqlclient
```
