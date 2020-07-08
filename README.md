Ranking
===========

## About
    This project aims to list the teams with the most famous instagram accounts.
 ```
 
## Installation

You can create a virtual environment and install the required packages with the following commands:

```bash
    $ virtualenv env                        # Create a virtual environment called env
    $ source env/bin/activate               # Activate the environment
    (env) $ pip install -r requirements.txt # Install the required packages
```

```
in http://127.0.0.1:8000/ you can see ranking top ten team.
in http://127.0.0.1:8000/nfl/teams/ you can see ranking of nfl teams.
in http://127.0.0.1:8000/football/premier_league/teams/ you can see ranking of premier league teams.
in http://127.0.0.1:8000/football/la_liga/teams/ you can see ranking of la liga teams.
```

Setup the database:

```bash
    (env) $ python manage.py makemigrations
    (env) $ python manage.py migrate
```

Run crawlers:
```bash
    (env) bash crawlers.bash
```

Run the server:

```bash
    (env) $ python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000`


