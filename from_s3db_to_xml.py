#!/usr/bin/env python3

import sqlite3
from lxml import etree


def from_s3db_to_xml(file_path):
    """Generate json file from sqlite3 file given in input."""

    to_file = file_path.replace('.s3db', '.xml')
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    count = 0
    xml_string = "<convoy> </convoy>"
    convoy = etree.fromstring(xml_string)
    for data in cur.execute('select * from convoy;'):
        if data[4] <= 3:
            vehicle = etree.SubElement(convoy, "vehicle")
            vehicle_id = etree.SubElement(vehicle, "vehicle_id")
            engine_capacity = etree.SubElement(vehicle, "engine_capacity")
            fuel_consumption = etree.SubElement(vehicle, "fuel_consumption")
            maximum_load = etree.SubElement(vehicle, "maximum_load")
            vehicle_id.text = str(data[0])
            engine_capacity.text = str(data[1])
            fuel_consumption.text = str(data[2])
            maximum_load.text = str(data[3])
            count += 1

    tree = etree.ElementTree(convoy)
    tree.write(to_file)
    if count in (0, 1):
        print(f"{count} vehicles were saved into {to_file}")
    else:
        print(f"{count} vehicles were saved into {to_file}")

        return to_file
