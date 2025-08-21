#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull saimaniroopm1609/django-cicd-project:latest

# Run the Docker image as a container
docker run -t -p 8000:8000 saimaniroopm1609/django-cicd-project:latest
