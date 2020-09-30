FROM python:3.5-slim-buster
WORKDIR /work-schedule-gen
COPY . .
RUN pip3 install -r requirements.lock
WORKDIR /work-schedule-gen/app
