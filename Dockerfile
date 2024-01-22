FROM python:3.10

WORKDIR /app

COPY ./app ./app
COPY requirements.txt .
COPY ./flag.txt /flag.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
