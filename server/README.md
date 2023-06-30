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

```
docker compose run --entrypoint="python" backend manage.py load_countries --file_path raw-data/dictionary.csv
```

# TODO: UPDATE ME
