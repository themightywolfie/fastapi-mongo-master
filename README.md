# Web Server

## Overview

This application is a web server that ingests JSON formatted log data, for example

```
[
   {"time":1685426738,"log":"lorem1 lipsm"},
   {"time":1685426739,"log":"lorem2 lipsm"},
   {"time":1685426740,"log":"lorem3 lipsm"}
]
```

The data is stored in a MongoDB database. One can also search for the stored data.

The web server is created using FastAPI. The data models are created using Pydantic which handles validations internally

## Endpoints

This server has two endpoints:

1. POST /ingest
    a. Accepts JSON data as specified in above examples

2. GET /query
    a. Searches for log data using query parameters like `/query?start=1685426738&end=1685426739&text=lorem`

## Software Requirements

1. Docker Desktop
2. Python 3.12 (if deploying locally)
3. MongoDB Community Server (if deploying locally)

## Deploy

##### via Docker Compose
1. Clone repo
2. Open terminal at root of the repo and run command `docker compose-up --build`

#### via Python

1. Clone repo
2. Create a `.env` file and add the line `DATABASE_URL=mongodb://localhost:27017`
2. Open terminal at root of the repo and run command `python main.py`

