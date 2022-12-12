import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .jobs import create_day

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(create_day, 'cron', hour=0)
    scheduler.start()