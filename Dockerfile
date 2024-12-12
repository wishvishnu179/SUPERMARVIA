FROM python:3.12-slim

WORKDIR /SUPERMARVIA

COPY . /SUPERMARVIA

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
