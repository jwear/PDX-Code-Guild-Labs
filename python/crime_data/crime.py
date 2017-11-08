import glob
import csv
from collections import namedtuple

filenames = glob.glob("*.csv")

# CrimeDataPoint = namedtuple('CrimeDataPoint', 'date', 'offense', )

def get_csv_data(filenames):
    for f in filenames:
        with open(f, 'r') as crime_file:
            csv_file = csv.reader(crime_file)
            csv_file = list(csv_file)
            column_headers = csv_file.pop(0)
            column_headers = [header.casefold().replace(' ', '_') for header in column_headers]
            # print(column_headers)

            row_data = []
            for row in csv_file:
                row_data.append(dict(zip(column_headers, row)))
            return row_data
