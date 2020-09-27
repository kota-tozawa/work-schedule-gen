FROM python:3.5-slim-buster

# Install dependencies:
COPY requirements.lock .
RUN pip3 install -r requirements.lock

# Run the application:
COPY app .
CMD ["python", "app/modules/main.py"]