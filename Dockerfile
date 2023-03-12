# Use an official Python runtime as a parent image
# FROM python:3.9-slim-buster
FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# ENV APP_HOME /app
# WORKDIR $APP_HOME
# COPY . ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variables
ENV API_ID=21210333
ENV API_HASH='13898900214f0a359b4f3bdad73d333f'

# Run the command to start the Pyrogram bot
CMD ["python", "main.py"]
