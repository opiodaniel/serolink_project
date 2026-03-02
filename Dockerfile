# Using bullseye-slim as base
FROM python:3.11.4-slim-bullseye

WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 1. Install System Dependencies for GeoDjango
# binutils is required for find_library() to work in Django
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip and install Python requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy project files
COPY . /app

# 4. Create a custom entrypoint script to automate migrations
# We do this because Render Free Tier doesn't allow manual Shell access
RUN printf "#!/bin/sh\npython manage.py migrate --noinput\ngunicorn serolink.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:10000" > /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Start the app via the entrypoint script
CMD ["/app/entrypoint.sh"]