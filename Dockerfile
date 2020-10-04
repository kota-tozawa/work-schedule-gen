FROM python:3.6-slim-buster
WORKDIR /work-schedule-gen
COPY . .
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv sync
WORKDIR /work-schedule-gen/app