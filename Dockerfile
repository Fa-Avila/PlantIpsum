# Use an official Python runtime as a parent image
FROM python:2.7-alpine

# create new user to run app
RUN adduser -D PlantIpsum

# Set the working directory to /home/plantIpsum
WORKDIR /home/PlantIpsum

COPY requirements.txt requirements.txt
RUN pip install virtualenv
RUN virtualenv venv

RUN apk update && apk --no-cache add build-base
RUN pip install numpy==1.16.2

RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY plantipsum.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP plantipsum.py

RUN chown -R PlantIpsum:PlantIpsum ./
USER PlantIpsum

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

#CMD tail -f /dev/null
