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
$ FLASK_ENV=development flask run
```
### production
```shell
$ FLASK_ENV=production flask run
```

## How to run tests
```shell
$ python3 -m unittest
```

## API specification
The documentation is made with swagger. 
Navigate the base url of the api in the root. http://127.0.0.1:8000
