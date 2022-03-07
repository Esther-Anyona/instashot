# Project Title
### instashot
## Description
This is a django web application of a clone of the website for the popular photo app Instagram

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
1. git clone the repository
    - https://github.com/esther-anyona/instashot.git
1. cd into app directory
    - cd instashot
1. create a virtual env
    -  python3 -m venv virtual
1. activate virtual environ
    - source virtual/bin/activate
1. Install all dependancies
1. Make Migrations
python3 manage.py makemigrations
    - Apply migrattions to database
    - python3 manage.py migrate
1. To run the app
    - python3 manage.py runserver

### Prerequisites

The application requires the following installations to operate:

* pip
* gunicorn
* django
* psycopg2

### Requirements
The user can perform the following functions:

- Sign in to the application to start using it.
- Upload pictures to the application.
- See their profile with all their pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.
- A user can search for other users names on the application.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system
1. run python3 manage.py test

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With
* Python 4.0.3

## Authors
This was a solo project.

## Bugs
There are no known bugs at the moment but should you spot one, feel free to create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc