# Use official Python 3.12 image
FROM mcr.microsoft.com/devcontainers/python:3.12

COPY ./requirements.txt /tmp/requirements.txt

# Install Python dependencies and system dependencies, then clean up in a single RUN command
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apt-get update && \
    apt-get install -y sqlite3 && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Set default user to vscode
USER vscode
