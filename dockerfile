FROM python:3.14
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]

COPY test_app.py .
CMD ["python", "test_app.py"]