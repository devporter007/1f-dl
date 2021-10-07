FROM python:3.9

WORKDIR /app

RUN pip install beautifulsoup4 requests

COPY main.py .

ENTRYPOINT ["python", "main.py"]
