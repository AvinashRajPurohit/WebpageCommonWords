# Webpage Common Words


## Requirements
  * Python-version -: Python 3.9.9
  * Django-version -: 4.0.0

```sh
$ python3 -V
$ django-admin --version
```
## Setup

The first thing to do is to clone the repository:
```sh
$  git clone https://github.com/AvinashRajPurohit/WebpageCommonWords.git
$  cd dir_name
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ sudo apt install python3-venv
$ python3 -m venv env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`
NOTE: go through with why.txt to know approachs.
NOTE: Will not prefer to use create api in swagger it might hang with large html data for that can use drf ui


 

