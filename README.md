# Bank Authenticator (Docker-ready)

A small Flask + Streamlit project for bank-note authentication using a pre-trained classifier.

## Contents
- `flasgger_app.py` — Flask API with Swagger UI (container entrypoint)
- `flask_app.py` — minimal Flask app
- `streamlit_app.py` — Streamlit UI
- `classifier.pkl` — trained model (kept in repo)
- `requirements.txt` — Python dependencies
- `Dockerfile` — image build instructions

## Build and run locally

Build the image:

```bash
docker build -t bank-auth-app .
```

Run the container (exposes Flask on port 5000):

```bash
docker run -p 5000:5000 bank-auth-app
```

Then open `http://localhost:5000/apidocs` for the Flasgger UI.

## Publish to GitHub

1. Create a GitHub repository and push your branch.
2. Enable GitHub Packages permissions for the repo if you plan to publish to GHCR.

## Notes
- Large or private datasets (`*.csv`, notebooks) are excluded from the Docker image by `.dockerignore` but remain in the repo per your request.
- If you prefer the image to contain the data, remove those entries from `.dockerignore`.