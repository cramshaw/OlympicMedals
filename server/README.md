# Olympic Medal Backend

This is a Python Django backend application providing a backend for serving data for the Olympic Medal table.

## Quick Start

Docker Compose can be used to bring up the backend application.

1. First, build the docker image:

```
cd server
docker build . -t olympics-be
```

### Docker shell

The following steps can be approached from your command line. Alternatively, to speed things up slightly, shell into the backend docker container with `docker compose run --rm --entrypoint="bash" backend` and then run all commands replacing `docker compose run --rm backend` with just `python`.

### Native shell

2. Migrate the database:

```
docker compose run --rm backend manage.py migrate
```

3. Load data into the database:

First load the countries dictionary

```
 docker compose run --rm backend manage.py load_countries --file_path=raw-data/dictionary.csv
```

Then load the medal data:

```
docker compose run --rm backend manage.py load_medals --file_path=raw-data/2004-2012.csv
```

4. (Optional) Create a superuser

If you want to make use of the admin interface, this is a good time to create a superuser by running and then following the prompts:

```
docker compose run --rm backend manage.py createsuperuser
```

5. Start the application

Everything should now be in place and you can start the backend by returning to the root directory and running:

```
cd ..
docker compose up
```

This will start a dev server and make it available at [http://localhost:8000/](http://localhost:8000/).

## Development

Tests are written using pytest. They rely on database access, and assuming all steps above have been followed can most easily be run inside a docker container shell with:

```
pytest
```

## Notes

In the original dataset there were some challenges. These are documented below:

- Countries with mismatched codes

Two countries had more than 1 country code in the provided dictionary. Both were fixed to use the single, internationally recognised code. For reference these were:

    - Romania - ROM => ROU
    - Serbia - SCG => SRB

- Pending results

One result was marked as 'pending'. As this is an unawarded medal and would not be able to feature in the table, it was removed from the dataset.

- Mixed events

In order to produce the most accurate table possible, events where multiple athletes win medals, but the medal only counts as a single medal for the country, have been aggregated. However, the dataset provided offers no way to distinguish this in the case mixed doubles events (Badminton and Tennis). Therefore this is currently a known issue with the data loading and would require further investigation to determine a better resolution.

## Admin

If you have created a superuser, and the application is running, you can log into admin to view and edit the data at:
[http://localhost:8000/admin](http://localhost:8000/admin)

## API docs

The API is provided using Django Rest Framework and can be browsed.

```
Medal Table View

/api/v1/medal-table/<YEAR>/

Return value: [<Country>]

Country:
    country_name: string
    country_code: string
    gold_medal_count: integer
    silver_medal_count: integer
    bronze_medal_count: integer

Example:

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
