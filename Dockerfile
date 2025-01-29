FROM python:3.11-slim

WORKDIR /app

COPY /app /app

RUN pip install --no-cache-dir flask pytest

EXPOSE 5000

CMD ["python", "app.py"]
