
# FastApi Postgresql CRUD


OPTIONAL 

## Build Container and image in Docker 
docker-compose -f docker-compose.yml build

## Run image in Docker 
docker-compose -f docker-compose.yml up

## RUN PROJECT ONLY IN PYTHON

Before to start, you need to install the dependencies:
`pip install -r requirements.txt`

To have a local env without docker it is recommended to use the following commands:

1.  .\venv\Scripts\activate
2. cd .\app\

## To run Project:

    uvicorn main:app --reload

To be able to see the documentation in swagger in the url:
`http://127.0.0.1:8000/swagger/`

