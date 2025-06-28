from apscheduler.schedulers.background import BackgroundScheduler
from app.invoiceGenerator import emitir_invoices

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(emitir_invoices, 'interval', hours=3)
    scheduler.start()