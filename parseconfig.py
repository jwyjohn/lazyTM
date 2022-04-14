from joinmeeting import *
import yaml
import schedule
import time
import datetime

def clock():
    # 用于在log里打印时钟
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('[CLOCK] ﾟ ∀ﾟ)ノ {} '.format(ts))


def task_closure(name,cid,pwd):
    # 返回一个加入会议的函数
    def task():
        print("[INFO] (*ﾟ∇ﾟ) {} entering meeting {}:{}!".format(name,cid,pwd))
        try:
            enter_meeting(cid, pwd, "mewo~")
        except:
            print("[ERRO] Σ( ﾟдﾟ) {} failed enter meeting {} !".format(name,cid))

    return task

def read_curr(filename):
    # 读yaml，然后按要求返回一个Scheduler
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
