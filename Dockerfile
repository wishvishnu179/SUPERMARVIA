FROM python:3.9-slim-buster
WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . /app
CMD gunicorn app:app & python3 bot.py
