# ScreenRecorder

Record your screen for X minuts every X minuts, kepp only last Y video files and saves outputs at your desired location

it's a full Pycharm project you probably not gonna need all of it

run example:

main_example.py

if __name__ == '__main__':
    start(10, r'c:\temp', 3) # start record (will record 10 min video file every 10 min, and keep only last 3)
    time.sleep(60 * 5) # run some another process
    Envar.set('false')# stop recording (will stop in the end of last recording cycle)
    print("stop video")
