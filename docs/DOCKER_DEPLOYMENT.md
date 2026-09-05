# Docker Deployment Guide

This document explains how to run the Customer Churn & LTV Prediction API using Docker.

## Prerequisites

Before running the application, make sure Docker is installed and running.

Verify Docker installation:

```bash
docker --version

Build the Docker Image

Navigate to the project root directory and run:

docker build -t churn-api .

This command creates a Docker image named churn-api.

Run the Docker Container

Run the following command:

docker run -p 8001:8000 churn-api
Port Mapping

The application runs on port 8000 inside the Docker container.

The command maps:

Host Port 8001 → Container Port 8000

Therefore, the API can be accessed from the host machine at:

http://127.0.0.1:8001
Access Swagger UI

After the container starts successfully, open:

http://127.0.0.1:8001/docs

Swagger UI can be used to test the following endpoints:

GET /
GET /health
POST /predict
POST /batch_predict
Deployment Verification

The deployment was verified by:

Building the Docker image successfully.
Running the Docker container successfully.
Verifying port mapping.
Accessing Swagger UI through the host machine.
Testing all API endpoints inside the containerized environment.
Result

The Customer Churn & LTV Prediction API was successfully containerized and executed using Docker.