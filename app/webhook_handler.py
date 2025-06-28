import starkbank.transfer
import starkbank
import starkbank.event
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starkbank import Project, Transfer
from starkbank.error import InvalidSignatureError
from dotenv import load_dotenv
import os
import logging

# Configura logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

project_id = os.getenv("PROJECT_ID")
private_key_path = os.getenv("PRIVATE_KEY_PATH")
private_key_path = os.path.abspath(private_key_path)

# Lê chave privada
with open(private_key_path, "r") as f:
    private_key = f.read()

# Autentica projeto
project = Project(
    id=project_id,
    private_key=private_key,
    environment="sandbox"
)
import starkbank
starkbank.user = project


async def handle_webhook(request: Request):
    try:
        payload = await request.body()
        signature = request.headers.get("Digital-Signature")

        if not signature:
            logger.warning("Request sem cabeçalho Digital-Signature")
            raise HTTPException(status_code=400, detail="Missing Digital-Signature header")

        # Valida evento e parseia
        event = starkbank.event.parse(
            content=payload.decode("utf-8"),
            signature=signature
        )

        logger.info(f"Evento recebido: id={event.id} subscription={event.subscription} type={event.log.type}")

        # Processa evento do tipo 'credited'
        if event.subscription == "invoice" and event.log.type == "credited":
            invoice = event.log.invoice

            fee = int(invoice.fee or 0)
            interest = int(invoice.interest or 0)
            fine = int(invoice.fine or 0)
            net_amount = invoice.amount - (fee + interest + fine)
            transfer = Transfer(
                amount=net_amount,
                bank_code="20018183",
                branch_code="0001",
                account_number="6341320293482496",
                tax_id="20.018.183/0001-80",
                name="Stark Bank S.A.",
                account_type="payment"
            )

            starkbank.transfer.create([transfer])

            logger.info(f"💸 Invoice {invoice.id} creditada. Transferido R${net_amount/100:.2f}")
            return JSONResponse(content={"status": "success"}, status_code=200)

        logger.info("Evento ignorado.")
        return JSONResponse(content={"status": "ignored"}, status_code=200)

    except InvalidSignatureError:
        logger.error("Assinatura digital inválida")
        raise HTTPException(status_code=400, detail="Invalid signature")

    except Exception as e:
        logger.exception("Erro interno no webhook")
        raise HTTPException(status_code=500, detail=str(e))
