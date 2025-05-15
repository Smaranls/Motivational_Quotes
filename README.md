## Motivational Quotes API

Welcome to the **Motivational Quotes API** — a simple yet powerful RESTful API that delivers inspirational and motivational quotes programmatically.

---

## What This Project Does

This API serves motivational quotes in JSON format to help developers, educators, and enthusiasts add daily inspiration into their applications, websites, or services.

Built using **FastAPI** for high performance and ease of development, the project is fully **Dockerized** for consistent deployment and uses **GitHub Actions** for automated testing, linting, and Docker image builds. Documentation is powered by **MkDocs** for easy navigation and clarity.

---

## Features

- RESTful API delivering motivational quotes as JSON  
- FastAPI backend for fast, asynchronous, and easy development  
- Dockerized for consistent and simple deployment  
- Automated CI/CD with GitHub Actions for testing, linting, and building Docker images  
- Comprehensive documentation using MkDocs  

---

## How to Run Locally

### 1. Clone the repository

git clone https://github.com/yourusername/motivational-quotes-api.git
cd motivational-quotes-api

### 2.  Set up virtual environment and install dependencies

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

### 3.  Run the FastAPI app locally

```uvicorn main:app --reload`
---
## How to Run Using Docker

### 1. Build the Docker image

docker build -t motivational-quotes-api .

### 2.  Run the Docker container

docker run -p 8000:8000 motivational-quotes-api

### 3. Access the API

http://localhost:8000/docs

---
