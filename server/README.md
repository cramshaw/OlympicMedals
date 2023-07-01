- Build backend docker image

```
cd server
docker build . -t olympics-be
```

- run migrations

- docker compose up

:boom:

# Loading data

# TODO: Update command

# MUST RUN LOAD COUNTRIES BEFORE LOAD MEDALS

# COMBINE SCRIPTS?

```
docker compose run --entrypoint="python" backend manage.py load_countries --file_path raw-data/dictionary.csv
```

```
docker compose run --entrypoint="python" backend manage.py load_medals --file_path raw-data/2004-2012.csv
```

# TODO: UPDATE ME

# Creating a user/viewing admin
