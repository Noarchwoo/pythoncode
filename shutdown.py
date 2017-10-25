# set the time to shutdown the computer

import time
from os import system
import subprocess
import datetime


running = True

flag = True

while flag:
    hour = int(raw_input('hour: '))
    minute = int(raw_input('minute: '))

    now = datetime.datetime.now()

    h = int(now.hour)
    m = int(now.minute)
    print hour, h, minute, m
    if hour >= h and minute >= m:
        flag = False
        sep = (hour-h)*3600 + (minute-m)*60
        time.sleep(sep)
        print 'shutting down...'
        subprocess.call(['shutdown', '/s'])
    else:
        print 'sorry, now is over %d:%d' %(hour, minute)
        print 'try another time'


