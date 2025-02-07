import csv

def create_database():
    with open('app_tracking.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Time', 'Application']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

