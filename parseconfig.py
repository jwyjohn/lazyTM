from joinmeeting import *
import yaml
import schedule
import time
import datetime

def clock():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('[CLOCK]', ts)


def task_closure(name,cid,pwd):
    def task():
        print("[INFO] {} entering meeting {}:{}!".format(name,cid,pwd))
        try:
            enter_meeting(cid, pwd, "mewo~")
        except:
            print("[ERRO] {} failed enter meeting {} !".format(name,cid))

    return task

def read_curr(filename):
    with open(filename, encoding='utf-8') as f:
        curr = yaml.load(f, Loader=yaml.FullLoader)
    sche = schedule.Scheduler()
    sche.every(1).seconds.do(clock)
    for course in curr['courses']:
        print(course)
        this_task = task_closure(course['name'],course['cid'],course['pwd'])
        print(this_task)
        getattr(sche.every(), course['weekday']).at(course['time']).do(this_task)
    return sche
