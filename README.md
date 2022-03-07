# Wzh API

![technology Python](https://img.shields.io/badge/technology-python-blue.svg)

Wzh API is an RESTFul API using python to technical evaluation.

## Installation

### Requirements
- Python 3.6 and newer.

### Setup

#### Create an environment
```shell
$ python3 -m venv venv
```

#### Activate the environment
```shell
$ . venv/bin/activate
```

#### Install dependencies
```shell
$ pip3 install -r requirements.txt
```

## How to run app

### local
```shell
$ FLASK_ENV=development FLASK_APP=app/__main__ venv/bin/flask run
```
### production
```shell
$ FLASK_ENV=production FLASK_APP=app/__main__ venv/bin/flask run
```
or
```shell
$ gunicorn app.__main__:app
```

## How to run tests
```shell
$ python3 -m unittest
```

## API specification
The documentation is made with swagger.
- It can be viewed by navigating to the base url, root. of the API. http://127.0.0.1:8000
- Or, It can also use swagger editor with [swagger.json]

[swagger.json]: https://raw.githubusercontent.com/pgarduino/wzh-api/master/doc/specs/swagger.json

