#!/usr/bin/env python

from from_xlsx_to_csv import from_xlsx_to_csv
from pre_processing import pre_process
from sqlite3_db import pre_processed, db_operation
from from_s3db_to_json import is_sqlite3_file, from_s3db_to_json
from from_s3db_to_xml import from_s3db_to_xml

file = input("Input file name\n")

if not is_sqlite3_file(file):
    if not pre_processed(file):
        if file.endswith('.xlsx'):
            csv_file = from_xlsx_to_csv(file)
        else:
            csv_file = file

        checked_file = pre_process(csv_file)
    else:
        checked_file = file

    s3db_file = db_operation(file, checked_file)
else:
    s3db_file = file

json_file = from_s3db_to_json(s3db_file)
xml_file = from_s3db_to_xml(s3db_file)
