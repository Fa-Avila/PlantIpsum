# Use an official Python runtime as a parent image
FROM python:2.7-alpine

# create new user to run app
RUN adduser -D PlantIpsum

# Set the working directory to /home/plantIpsum
WORKDIR /home/PlantIpsum

# Copy app requirements into working directory
COPY requirements.txt requirements.txt

# Install virtualenv
RUN pip install virtualenv

# Setup virtual environment named venv
RUN virtualenv venv

# Update apk
RUN apk update && apk --no-cache add build-base

# Install numpy
RUN pip install numpy==1.16.2

# Install Requirements
RUN venv/bin/pip install -r requirements.txt

# Install gunicorn
RUN venv/bin/pip install gunicorn

# Copy app folder to app folder in working directory
COPY app app

# Copy plantipsum.py config.py boot.sh into working directory
COPY plantipsum.py config.py boot.sh ./

# Add execute permision to boot.sh
RUN chmod +x boot.sh

# Add environment variable FLASK_APP
ENV FLASK_APP plantipsum.py

# Changes the owner of file to new user PlantIpsum
RUN chown -R PlantIpsum:PlantIpsum ./

# Change to non root user PlantIpsum
USER PlantIpsum

# Expose port 5000 
EXPOSE 5000

# Setting image's main command to boot.sh
ENTRYPOINT ["./boot.sh"]
