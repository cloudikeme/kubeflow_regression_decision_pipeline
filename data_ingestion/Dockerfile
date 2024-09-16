# Use a specific version of Python for better reproducibility
FROM python:3.8.16-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY data_ingestion.py .

# Run as non-root user for better security
RUN useradd -m appuser
USER appuser

# Set the entrypoint
ENTRYPOINT ["python", "data_ingestion.py"]