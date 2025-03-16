# Use official Python 3.12 image
FROM mcr.microsoft.com/devcontainers/python:3.12

COPY ./requirements.txt /tmp/requirements.txt
# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt
# Clean up
RUN rm /tmp/requirements.txt


# Install system dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Install Python dependencies
RUN pip install --upgrade pip && pip install \
    panel holoviews bokeh hvplot param \
    mypy pytest black ruff

# Set default user to vscode
USER vscode
