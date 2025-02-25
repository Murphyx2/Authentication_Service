# Use official Python runtime as base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# expose
EXPOSE 8000

# Run migrations and start the server
CMD ["sh", "-c", "python ./manage.py migrate && gunicorn --bind 0.0.0.0:8000 auth_service.wsgi"]
