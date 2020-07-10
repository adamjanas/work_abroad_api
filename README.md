## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Launch](#launch)

## General info
This is the repository of work_abroad's api. This project is intended for offering and finding jobs all around the world.
Literally "earn and learn".
Project provides registration, offering, applying and reviewing (users, offers).


## Technologies
Project is created with: \
* [django](https://www.djangoproject.com) \
* [django rest framework](https://www.django-rest-framework.org) \
* [poetry](https://python-poetry.org) \
* [postgresql as DB Engine](https://www.postgresql.org) \
* [docker](https://www.docker.com)

## Launch
[poetry](https://python-poetry.org) is a package-manager tool of the project.


Create appropriate directory for the project and inside generate virtual environment

```bash
$ cd ../project_directory
$ poetry new <project_name>
```


Activate virtual environment, clone repository to your local machine and install dependencies from Pipfile.lock

```bash
$ poetry shell
$ git clone <repo_address>
$ poetry install
```


If you need help or more info about poetry, run:

```bash
$ poetry --help
```