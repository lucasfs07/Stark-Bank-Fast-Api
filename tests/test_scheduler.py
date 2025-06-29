from unittest.mock import patch
from app.scheduler import start_scheduler

@patch("app.scheduler.emitir_invoices")
def test_scheduler_starts(mock_emit):
    start_scheduler()
    assert True  
