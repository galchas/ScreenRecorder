import json
from ScreenRecorder import ScreenRecorder
import os


class Envar:

    @staticmethod
    def is_working():
        Envar._validate_file()
        with open('data.json') as json_file:
            data = json.load(json_file)
            return data['work'] == 'true'

    @staticmethod
    def set(state):
        Envar._validate_file()
        with open('data.json', 'r+') as f:
            data = json.load(f)
            data['work'] = state  # <--- add `id` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()  # remove remaining part

    @staticmethod
    def _validate_file():
        if not os.path.exists('data.json'):
            with open('data.json', 'w') as f:
                f.write('{"work" : "true"}')
                f.close()


#record to new file every 'record_time' and save them in records_path until Envar.is_working() is false
def start(record_time, records_path, save_last):
    Envar.set('true')  # start record
    while True:
        sr = ScreenRecorder(time_min=record_time, records_path=records_path, records_to_keep=save_last)
        sr.record()
        if not Envar.is_working():
            break
    print ("recorded terminated! :)")


if __name__ == '__main__':
    start()



