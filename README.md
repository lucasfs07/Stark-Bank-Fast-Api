# 🚀 Stark Bank Webhook API (FastAPI)

[![FastAPI](https://img.shields.io/badge/FastAPI-async%20framework-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![GCP Cloud Run](https://img.shields.io/badge/Google%20Cloud-Run-blue?logo=googlecloud)](https://cloud.google.com/run)

API criada com **FastAPI** para receber **webhooks da Stark Bank**, emitir invoices e executar tarefas automáticas agendadas. Implantada com **Google Cloud Run**.

---

## 🧩 Funcionalidades

- ✅ Recebimento de webhooks de eventos da Stark Bank
- 🧾 Emissão automatizada de invoices via SDK
- ⏱️ Scheduler com tarefas periódicas usando APScheduler
- ☁️ Deploy automatizado no Google Cloud Run
- 🐳 Docker Ready

---

## 📁 Estrutura do Projeto

```bash
starkbank-webhook/
│
├── app/
│   ├── main.py               # Inicializa a API
│   ├── webhook_handler.py    # Processamento de webhooks
│   └── scheduler.py          # Agendador de tarefas
├── tests/                    # testes unitarios
|   ├── test_invoiceGenerator.py  
|   ├── test_scheduler.py
|   ├── test_Webhook_handler.py
├── requirements.txt          # Dependências
├── Dockerfile                # Configuração da imagem Docker
├── .env                      # Variáveis de ambiente
└── README.md                 # Este documento
```

---

## ⚙️ Como Rodar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/starkbank-webhook.git
cd starkbank-webhook
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 2.1 (Opcional)

Recomendamos usar o uvicorn + ngrok em seu ambiente virtual!

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute localmente

```bash
uvicorn app.main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para testar a API via Swagger UI.

---

## 🐳 Docker

### Build da imagem

```bash
docker build -t starkbank-webhook .
```

### Rodar localmente

```bash
docker run -p 8080:8080 starkbank-webhook
```

---

## ☁️ Deploy no Google Cloud Run

### 1. Configure o SDK:

```bash
gcloud auth login
gcloud config set project fluent-justice-428721-p5
gcloud config set run/region europe-west1
```

### 2. Deploy

```bash
gcloud run deploy stark-bank-fast-api --source . --platform managed --allow-unauthenticated
```

---

## 📩 Webhook

- Endpoint ativo: `POST /webhook`
- Configure esse path no painel da Stark Bank.
- Exemplo de URL no Cloud Run:

```
https://stark-bank-fast-api-xxxxx.a.run.app/webhook
```

---

## 🔐 Variáveis de Ambiente

Exemplo do arquivo `.env`:

```
STARKBANK_PROJECT_ID=your_project_id
STARKBANK_PRIVATE_KEY_PATH=./private-key.pem
```

---

## 📆 Scheduler

- Executado automaticamente ao iniciar a aplicação (`startup_event`)
- Exemplo: emissão de invoices aleatórias com APScheduler

---

## 📘 Referências

- [Stark Bank SDK (Python)](https://github.com/starkbank/sdk-python)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Cloud Run](https://cloud.google.com/run)
- [APScheduler](https://apscheduler.readthedocs.io/)

---

## 👤 Autor

**Lucas Fernando**  
🔗 [LinkedIn](https://www.linkedin.com/in/lucasxfernando/)  
💼 Banco Pan • Integrações, APIs, Antifraude, Pagamentos

---

## ⚠️ Licença

Projeto privado. Para fins de teste e integração com Stark Bank.
