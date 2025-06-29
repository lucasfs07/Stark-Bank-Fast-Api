import pytest
from app.invoiceGenerator import emitir_invoices

def test_emitir_invoices_returns_invoices():
    invoices = emitir_invoices()
    assert isinstance(invoices, list)
    assert len(invoices) > 0
    for invoice in invoices:
        assert hasattr(invoice, "amount")
        assert hasattr(invoice, "name")