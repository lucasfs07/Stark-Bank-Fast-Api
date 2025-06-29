from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
#teste assinatura dgital
@patch("starkbank.event.parse")
def test_webhook_credited_event(mock_parse):
    mock_event = MagicMock()
    mock_event.id = "mock_event_id"
    mock_event.subscription = "invoice"
    mock_event.log.type = "credited"
    mock_event.log.invoice.amount = 10000
    mock_event.log.invoice.fee = 500
    mock_event.log.invoice.interest = 0
    mock_event.log.invoice.fine = 0
    mock_event.log.invoice.id = "mock_invoice_id"

    mock_parse.return_value = mock_event

    payload = {
        "subscription": "invoice",
        "log": {
            "type": "credited",
            "invoice": {
                "amount": 10000,
                "fee": 500,
                "interest": 0,
                "fine": 0,
                "id": "mock_invoice_id"
            }
        }
    }
    headers = {
        "Digital-Signature": "qualquer_coisa"
    }

    response = client.post("/webhook", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
