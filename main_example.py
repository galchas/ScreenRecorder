import time
from RecordCycle import Envar, start


if __name__ == '__main__':
    start(10, r'c:\temp', 3) # start record (will record 10 min video file every 10 min, and keep only last 3)
    time.sleep(60 * 5) # run some another process
    Envar.set('false')# stop recording (will stop in the end of last recording cycle)
    print("stop video")
