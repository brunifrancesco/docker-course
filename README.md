# Install everything

    python3 -m venv venv
    source bin/activate
    pip install -r requirements.txt

# Getting started: Mongo volume

Create an empty folder called *data*:
  
    mkdir data

# RUN the application locally

    uvicorn main:app --reload

# Pull up component with Docker compose

    docker-compose up --build

# Sample calls

Chane port and host accordingly

## Get students

    curl http://localhost:1980

## Create new student

    curl -XPOST -H "Content-Type: application/json" -d '{"fullname":"Francesco"}' http://localhost:1980/
