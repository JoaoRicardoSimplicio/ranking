Rankinkg
=======

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


