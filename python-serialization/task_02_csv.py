#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save to data.json."""
    try:
        with open(csv_filename, 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
