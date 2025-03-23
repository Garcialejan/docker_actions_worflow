FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requierements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"]