#!/usr/bin/env python3

import sqlite3
import json


def is_sqlite3_file(file_path):
    """Check if the file given in input is sqlite3 file."""

    return file_path.endswith('.s3db')


def from_s3db_to_json(file_path):
    """Generate json file from sqlite3 file given in input."""

    to_file = file_path.replace('.s3db', '.json')
    convoy_dict = {}
    convoy = []
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    count = 0

    for data in cur.execute('select * from convoy;'):
        if data[4] > 3:
            convoy.append({"vehicle_id": data[0], "engine_capacity": data[1], "fuel_consumption": data[2], "maximum_load": data[3]})
            count += 1
    convoy_dict["convoy"] = convoy

    with open(to_file, 'w') as json_file:
        json.dump(convoy_dict, json_file)

    if count in (0, 1):
        print(f"{count} vehicle was saved into {to_file}")
    else:
        print(f"{count} vehicles were saved into {to_file}")

    return to_file
