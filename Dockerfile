FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose BOTH ports (main app and health check)
EXPOSE 8080
EXPOSE 8081

COPY . /app

# Separate processes:
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
