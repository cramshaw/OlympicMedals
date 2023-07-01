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

# Notes

Romania - ROM ROU
Serbia - SCG SRB
Pending results
Mixed events

# Creating a user/viewing admin

# API docs

/api/v1/medal-table/<YEAR>/

Returns

```
[
    {
        "country_name": "Argentina",
        "country_code": "ARG",
        "gold_medal_count": 1,
        "silver_medal_count": 2,
        "bronze_medal_count": 1
    }
]
```

# ADMIN
