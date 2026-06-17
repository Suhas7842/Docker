# Bank Authenticator

A bank-note authentication application built with Flask, Flasgger, Streamlit, and Docker. The project demonstrates Docker image creation, containerization, service orchestration with Docker Compose, and deployment of a machine learning model.

---

## Services

| Service | URL |
|----------|----------|
| Flasgger API | http://localhost:5000 |
| Swagger Documentation | http://localhost:5000/apidocs |
| Flask Prediction API | http://localhost:5001 |
| Streamlit UI | http://localhost:8501 |

---

## Project Structure

```text
.
├── flasgger_app.py
├── flask_app.py
├── streamlit_app.py
├── classifier.pkl
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── BankNote_Authentication.csv
├── TestFile.csv
└── ModelTraining.ipynb
```

### Files

- `flasgger_app.py` - Flask API with Swagger UI documentation
- `flask_app.py` - Flask prediction API
- `streamlit_app.py` - Streamlit frontend application
- `classifier.pkl` - Trained machine learning model
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image instructions
- `docker-compose.yml` - Multi-container service configuration

---

## Prerequisites

Install the following before running the project:

- Docker
- Docker Compose

Verify installation:

```bash
docker --version
docker compose version
```

---

## Run with Docker Compose (Recommended)

Build and start all services:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

View running services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

View logs for a specific service:

```bash
docker compose logs -f flasgger
```

Stop all services:

```bash
docker compose down
```

---

## Run with Docker

Build the Docker image:

```bash
docker build -t bank-auth-app .
```

Run the container:

```bash
docker run --rm -p 5000:5000 bank-auth-app
```

Open:

```text
http://localhost:5000
```

Swagger UI:

```text
http://localhost:5000/apidocs
```

---

## Docker Concepts Demonstrated

This project demonstrates:

- Dockerfile
- Docker Images
- Docker Containers
- Docker Compose
- Volume Mounting
- Container Networking
- Health Checks
- Multi-Service Applications

---

## Useful Docker Commands

List running containers:

```bash
docker ps
```

List Docker images:

```bash
docker image ls
```

Inspect a container:

```bash
docker inspect bank-auth-flasgger
```

Access a running container:

```bash
docker exec -it bank-auth-flasgger bash
```

Remove unused images:

```bash
docker image prune
```

---

## Troubleshooting

Rebuild images without cache:

```bash
docker compose build --no-cache
```

Restart services:

```bash
docker compose up --build
```

Check service status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

If ports `5000`, `5001`, or `8501` are already in use, stop the conflicting process or update the port mappings in `docker-compose.yml`.

---

## Learning Workflow

1. Build the image:

```bash
docker build -t bank-auth-app .
```

2. Run a single container:

```bash
docker run --rm -p 5000:5000 bank-auth-app
```

3. Stop the container.

4. Run the complete application stack:

```bash
docker compose up --build
```

5. Inspect logs and running containers.

6. Shut down services:

```bash
docker compose down
```