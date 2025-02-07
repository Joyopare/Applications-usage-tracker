import csv
import datetime

from database import create_database
from tracker import track_applications

def main():
    create_database()
    with open('app_tracking.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for app in track_applications():
            now = datetime.datetime.now()
            writer.writerow([now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S'), app])

if __name__ == '__main__':
    main()

