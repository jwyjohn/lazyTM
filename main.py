from joinmeeting import *
import schedule
import time
import datetime

def job():
    enter_meeting("***-***-***", "****", "cat")
def clock():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('[CLOCK]', ts)

schedule.every().tuesday.at("13:54").do(job)
schedule.every(1).seconds.do(clock)

while True:
    schedule.run_pending()
    time.sleep(0.5)