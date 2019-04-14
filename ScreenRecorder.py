import glob
import math
import os
import time
import numpy as np
import cv2
from PIL import ImageGrab
from win32api import GetSystemMetrics
import datetime


class ScreenRecorder:
    def __init__(self, time_min, records_path, records_to_keep=3):
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        self.cycle_time = time_min*60
        self.records_path = records_path
        self.records_to_keep = records_to_keep

    def record(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # you can use other codecs as well.
        start_time = time.time()
        file_name = r"{}.avi".format(datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d_%H-%M-%S'))
        vid = cv2.VideoWriter(file_name, fourcc, 8, (self.width, self.height))
        while True:

            img = ImageGrab.grab(bbox=(0, 0, self.width, self.height))  # x, y, w, h
            img_np = np.array(img)
            # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            vid.write(img_np)
            # cv2.imshow("frame", img_np)
            key = cv2.waitKey(1)
            now = time.time()
            if math.floor(now - start_time) >= self.cycle_time:
                break
        vid.release()
        self._manage_records()

    def _manage_records(self):
        record_list = [f.split('.')[0] for f in glob.glob("*.avi")]
        print record_list
        record_list.sort(key=lambda x: time.mktime(time.strptime(x, '%Y-%m-%d_%H-%M-%S')))
        # remove old record, keep only latest 3
        if len(record_list) > self.records_to_keep:
            record_name = r"{}.avi".format(record_list.pop(0))
            os.remove(os.path.join(self.records_path, record_name))
        print record_list


if __name__ == '__main__':

    sr = ScreenRecorder(time_min=1, records_path=r"C:\Users\admin\Desktop\Daily")
    sr.record()