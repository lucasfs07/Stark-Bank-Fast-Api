FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

# Comando para rodar a API FastAPI com uvicorn, ouvindo na porta 8080 (gcp)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
