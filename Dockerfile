FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY ./api /app/api