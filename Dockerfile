FROM python:3.5-slim-buster
COPY requirements.lock .
RUN pip3 install -r requirements.lock
COPY app .
CMD ["python", "main.py"]
