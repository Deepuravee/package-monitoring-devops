FROM python:3.10-slim

WORKDIR /app

COPY package_monitor.py .

RUN pip install prometheus_client

CMD ["python", "package_monitor.py"]
