FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn requests python-dotenv
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "9000"]
