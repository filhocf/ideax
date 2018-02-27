# How to install Idea X

## Introduction

Idea X is a Django application, so you can download it and install in a WSGI server or use a Docker image.

## Installation

### Get Idea X!
You can clone its repository or download a zip file.

### Install dependencies

### Database Configuration

Next thing we need to do is decide what database backend we'll use. The most common is MySQL but others are PostgreSQL and SQLite.
So once you decide, create a database with any name you want and grant privileges to a separate database user. It's recommended not to use an existing user or root.

With MySQL you can set up the database by issuing the following commands:
```
CREATE DATABASE ideax;
GRANT ALL PRIVILEGES ON ideax.* TO username@localhost IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

## Run with Docker

You can run IdeaX with SQLLite or a database server, like MySql. For the first, run the follow command, otherwise use the next instruction.
```
docker run -d -p 80:8000 --name ideax filhocf/ideax # run with sqlite3
```

```
docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=password mysql
docker run -d -p 80:8000 --name ideax --link mysql:mysql filhocf/ideax
```
