# Docker-Python-API-Endpoint

This repository contains a simple Python API endpoint Dockerized with Flask.

## Overview

This project demonstrates setting up a Flask-based API endpoint within a Docker container. It includes a basic Flask application that responds with "Hello, Docker!" to requests.

## Features

- **Flask Framework**: Utilizes Flask, a lightweight WSGI web application framework in Python.
- **Dockerized**: The application is containerized using Docker for easy deployment and scalability.
- **API Endpoint**: Provides a basic API endpoint `/api/hello` that responds with a JSON message.

## Requirements

- Docker
- Python 3.x

## Setup

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Docker-Python-API-Endpoint
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t dockerpy-api .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -p 5001:5000 dockerpy-api
   ```

4. **Access the API endpoint**:
   Open a web browser or use a tool like `curl` to access the API endpoint:
   ```bash
   curl http://localhost:5001
   ```

5. **Stop the container**:
   To stop the running container, press `Ctrl + C`.

## API Endpoint

- **URL**: `http://localhost:5001`
- **Method**: `GET`
- **Response**: JSON object `{ "message": "Hello, Docker!" }` (Example)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.
