from joinmeeting import *
from parseconfig import *
import time


schedule1 = read_curr('curriculum.yaml')

while True:
    schedule1.run_pending()
    time.sleep(0.5)