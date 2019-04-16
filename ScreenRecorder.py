import glob
import math
import os
import time
import numpy as np
import cv2
from PIL import ImageGrab
from win32api import GetSystemMetrics
from datetime import datetime
from RecordCycle import Envar


class ScreenRecorder:
    def __init__(self, time_min, records_path, records_to_keep=3):
        self._width = GetSystemMetrics(0)
        self._height = GetSystemMetrics(1)
        self.cycle_time = time_min*60
        self.records_path = records_path
        self.records_to_keep = records_to_keep
        self.stop = False

    def record(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # you can use other codecs as well.
        start_time = time.time()
        file_name = r"{}.avi".format(datetime.fromtimestamp(start_time).strftime('%Y-%m-%d_%H-%M-%S'))
        full_record_path = os.path.join(self.records_path, file_name)
        vid = cv2.VideoWriter(full_record_path, fourcc, 8, (self._width, self._height))
        try:
            while True:
                img = ImageGrab.grab(bbox=(0, 0, self._width, self._height))  # x, y, w, h
                img_np = np.array(img)
                # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
                vid.write(img_np)
                # cv2.imshow("frame", img_np)
                key = cv2.waitKey(1)
                now = time.time()
                if math.floor(now - start_time) >= self.cycle_time or self.stop:
                    break
        finally:
            vid.release()
            self._manage_records()

    @staticmethod
    def stop_record():
        Envar.set('false')
        print('Stop recording')

    def _manage_records(self):
        record_list = [str(f.split('.')[0].split('\\')[-1:]).replace("[\'", '').replace("']", '') for f in
                       glob.glob(os.path.join(r"C:\Users\admin\Desktop\Daily", "*.avi"))]
        if len(record_list) > 1:
            record_list.sort(key=lambda x:time.mktime(datetime.strptime(str(x), "%Y-%m-%d_%H-%M-%S").timetuple()))
        # remove old record, keep only latest 3
        if len(record_list) > self.records_to_keep:
            record_name = r"{}.avi".format(record_list.pop(0))
            full_path = os.path.join(self.records_path, record_name)
            if os.path.exists(full_path):
                os.remove(os.path.join(self.records_path, record_name))


if __name__ == '__main__':

    sr = ScreenRecorder(time_min=1, records_path=r"C:\Users\admin\Desktop\Daily")
    sr.record()
