# 1. Base image
FROM python:3.8.3-slim-buster

# 2. Copy files
COPY . /src

# 3. Install our deps
RUN pip install -r /src/requirements.txt
