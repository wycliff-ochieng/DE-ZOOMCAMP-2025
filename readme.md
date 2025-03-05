# DATA TALKS CLUB DATA ENGINEERING ZOOMCAMP 2025
## MODULE 1: Docker and Infastructure as a Code(Terraform)

**Dockerfile** is a script containing a set of instructions to automate the creation of Docker images. It defines the base image, dependencies, configurations, and commands to set up a containerized environment.

## Ingesting NY taxi data to postgres database
Utilized pandas to ingest chunks of 10000 rows of the data set into postgres db

### Dockerzing the ingestion script
Convert the jupyter notebook file into a python scripts
`jupyter nbconvert --to=script ingestion.ipynb`
`docker build -t taxi_ingestion:v001 .`
`docker run taxi_ingestion:v001 .`