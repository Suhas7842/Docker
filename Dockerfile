FROM python:3.12-slim

# Set a working directory
WORKDIR /usr/app

# Install build dependencies and runtime dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (dotfiles and large data excluded via .dockerignore)
COPY . /usr/app

EXPOSE 5000

# Use a non-root user where possible
RUN useradd --create-home appuser || true
USER appuser

CMD ["python", "flasgger_app.py"]
