FROM python:3.12.3-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /app/
# install system dependencies
RUN apt-get update && apt-get install -y libpq-dev build-essential
# install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN mkdir staticfiles

COPY . /app

ENTRYPOINT ["gunicorn", "API_JSON.wsgi", "-b", "0.0.0.0:8000"]
