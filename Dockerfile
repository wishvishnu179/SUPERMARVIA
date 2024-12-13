FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "supermarvia.wsgi:application"]
   
