import time
from RecordCycle import Envar, RecordCycle

if __name__ == '__main__':
    RecordCycle.start(10, r'c:\temp', 3) # start record (will record 10 min video file every 10 min, and keep only last 3)
    time.sleep(60 * 5) # run some another process
    RecordCycle.stop_recording()
    print("stop video")
