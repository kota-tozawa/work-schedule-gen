FROM python:3.5-slim-buster
WORKDIR /work-schedule-gen
COPY . .
RUN pip install --upgrade pip
RUN pip install -r prd-requirements.lock
WORKDIR /work-schedule-gen/app