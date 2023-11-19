FROM python:3.10
WORKDIR /app

ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

# Set the Gunicorn command to run on port 8000
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "interact.wsgi:application"]

