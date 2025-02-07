
import psutil
import datetime

def track_applications():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] not in ['System Idle Process', 'System']:
            yield proc.info['name']

