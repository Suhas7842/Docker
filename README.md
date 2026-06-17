# Bank Authenticator (Docker Learning Project)

This repo contains a small bank-note authentication project built with Flask, Flasgger, and Streamlit. It is configured for Docker and Docker Compose so you can learn container build, run, and service orchestration.

## Project overview

- `flasgger_app.py` — main Flask API with Swagger UI docs
- `flask_app.py` — alternate Flask app for prediction endpoints
- `streamlit_app.py` — Streamlit web UI for live prediction
- `classifier.pkl` — pre-trained scikit-learn model
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker image build instructions
- `docker-compose.yml` — service orchestration for Flask and Streamlit
- `.dockerignore` — files excluded from Docker image builds
- `BankNote_Authentication.csv`, `TestFile.csv` — dataset files used in the project
- `ModelTraining.ipynb` — notebook for model training / exploration

## Docker concepts in this repo

- `Dockerfile` builds a single Python image
- `docker-compose.yml` runs two services together:
  - `flask-api`
  - `streamlit-ui`
- Volume mounting is used for live code access
- Ports are published for external access

## Prerequisites

- Docker installed and running
- Docker Compose available (`docker compose`)
- Python installed only if you want to run locally without Docker

## Build the Docker image

From the repo root:

```bash
docker build -t bank-auth-app .
```

This builds the image using `Dockerfile` and installs dependencies from `requirements.txt`.

## Run the Docker image

Start the Flask container manually:

```bash
docker run --rm -p 5000:5000 bank-auth-app
```

Then open:

- `http://localhost:5000/apidocs` — Swagger UI for the Flask API

## Docker Compose commands

Start all services defined in `docker-compose.yml`:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

Stop and remove containers:

```bash
docker compose down
```

Rebuild images and restart services:

```bash
docker compose up --build
```

Show running containers for this compose project:

```bash
docker compose ps
```

View logs for all services:

```bash
docker compose logs -f
```

View logs for a specific service:

```bash
docker compose logs -f flask-api
```

## Service endpoints

- Flask API: `http://localhost:5000`
- Swagger UI: `http://localhost:5000/apidocs`
- Streamlit UI: `http://localhost:8501`

## Recommended workflow for learning Docker

1. Build the image:
   ```bash
docker build -t bank-auth-app .
```
2. Run the image locally:
   ```bash
docker run --rm -p 5000:5000 bank-auth-app
```
3. Stop the container and switch to Compose:
   ```bash
docker compose up --build
```
4. Inspect the service logs and behavior.
5. Stop Compose when done:
   ```bash
docker compose down
```

## Notes about datasets and .gitignore

- The repository currently includes `BankNote_Authentication.csv`, `TestFile.csv`, and `ModelTraining.ipynb`.
- Your `.gitignore` currently excludes `*.csv` and `*.ipynb`, so if you want to keep those files tracked in Git, remove those lines from `.gitignore`.
- The dataset files can be used by your app directly when mounted into a container.

## Troubleshooting

- If the container fails to start, check logs:
  ```bash
docker compose logs -f
```
- If port 5000 or 8501 is already in use, stop the conflicting service or change the published port.
- If requirements fail to install, verify `requirements.txt` and rebuild:
  ```bash
docker compose build --no-cache
```

## Learning tips

- Compare `docker run` vs `docker compose up`
- Inspect the built image layers with:
  ```bash
docker image ls
```
- Remove unused images with:
  ```bash
docker image prune
```
- Practice editing `docker-compose.yml` to add a new service or change environment variables

---

This README is intended as your Docker study guide for this project. Keep it updated as your app and Compose setup evolve.
