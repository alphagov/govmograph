#!/usr/bin/python3

import csv
import sys

try:
    if (sys.argv[1] == '-'):
        f = sys.stdin.read().splitlines()
    else:
        filename = sys.argv[1]
        f = open(filename, 'r')
    reader = csv.DictReader(f, delimiter='\t')
    with open('out.csv', 'w', newline='') as output_csvfile:
        fieldnames = ['from', 'to']
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        for row in reader:
            if (row['source_base_path'] != row['destination_base_path']):
                writer.writerow({'from': row['source_base_path'], 'to': row['destination_base_path']})
except Exception:
    print("Error Reading from file")
