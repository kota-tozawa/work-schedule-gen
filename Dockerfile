FROM python:3.5-slim-buster
WORKDIR /work-schedule-gen
COPY app .
COPY prd-requirements.lock .
RUN pip install -r prd-requirements.lock
WORKDIR /work-schedule-gen/app
