Ranking
===========

## Installation



You can create a virtual environment and install the required packages with the following commands:

```bash
    $ virtualenv env                        # Create a virtual environment called env
    $ source env/bin/activate               # Activate the environment
    (env) $ pip install -r requirements.txt # Install the required packages
```

Setup the database:

```bash
    (env) $ python manage.py makemigrations
    (env) $ python manage.py migrate
```

Run the server:

```bash
    (env) $ python manage.py runserver
```

```bash
    (env) bash crawlers.bash
```

The server will be available at `http://127.0.0.1:8000`


