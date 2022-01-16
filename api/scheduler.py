from apscheduler.schedulers.background import BackgroundScheduler
from .views import subscription_expire,age

#------------- Expire Subscription --------------
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(subscription_expire, 'interval', seconds=86400)
    scheduler.start()

#------------- Update Age --------------
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(age, 'interval', seconds=86400)
    scheduler.start()