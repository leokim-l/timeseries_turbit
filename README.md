# Small project about developing APIs for Turbi

## Task descritpion (refer to DESCRIPTION.md for more details):
Time Series Data Handling and API Development

Turbine 1: .csv file with `;` as a separator and two rows of header
Turbine 2: .csv file with `;` as a separator and two rows of header

Load time series data from the CSV files above into a MongoDB collection and make the data accessible through the FastAPI.

1. Data Preparation and Loading into MongoDB
Develop a python script to read the data from the CSV files and load it into a single MongoDB collection.

2. Add FastAPI Endpoint
Add an FastAPI endpoint that allows to retrieve the data based on turbine id and time ranges


## Usage

It is assumed that poetry and docker-compose are installed on the system. Once that is complete, after cloning the repository, change the relevant paths in docker-compose.yml and simply run, from the project folder:

```bash
docker-compose up -d
```

Then install the python dependencies, found in poetry.lock file, by running

```bash
poetry install
```

and from the directory timeseries/ import the data through

```bash
poetry run python import_data.py
```

Run the API by executing, from within the api/ folder:


```bash
poetry run uvicorn main:app --reload
```

Now the database is up and running. Open your browser at

http://127.0.0.1:8000/

and try to see what happens if looking the endpoint:

/1?startt=2016-01-01T00:00&endt=2016-01-01T18:50

where `1` is the turbine id and `startt` and `endt` are the beginning and end of the time range.

