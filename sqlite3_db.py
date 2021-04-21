#!/usr/bin/env python3
import sqlite3
import csv


def score(engine_capacity, fuel_consumption, maximum_load):
    """Return the score of a vehicle with respect to its characteristics."""

    needed_fuel = (int(fuel_consumption) / 100) * 450
    pit_stops = needed_fuel // int(engine_capacity)
    s = 0
    if int(maximum_load) >= 20:
        s += 2
    if needed_fuel <= 230:
        s += 2
    else:
        s += 1
    if pit_stops == 0:
        s += 2
    elif pit_stops == 1:
        s += 1

    return s


def pre_processed(file_path):
    """Check if a file has been pre-processed."""

    return file_path.endswith('[CHECKED].csv')


def db_insertion(cur, a, b, c, d, e):
    """Insert data to convoy table in sqlite3 database given a cursor object and a tuple of 5 elements."""

    cur.execute("INSERT INTO convoy(vehicle_id, engine_capacity, fuel_consumption, maximum_load, score) VALUES(?, ?, ?, ?, ?)", (a, b, c, d, e))


def db_operation(input_file, checked_file):
    """Insert data to sqlite3 database given a preprocessed file path."""

    db_name = checked_file.replace('[CHECKED].csv', '.s3db')
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("drop table if exists convoy;")
    conn.commit()
    cur.execute("""create table if not exists convoy(vehicle_id int primary key, engine_capacity integer not null, 
    fuel_consumption integer not null, maximum_load integer not null, score integer not null);""")
    conn.commit()
    with open(checked_file, newline='') as convoy:
        file_reader = csv.reader(convoy, delimiter=',')
        entries = 0
        if not pre_processed(input_file):
            for line in file_reader:
                db_insertion(cur, line[0], line[1], line[2], line[3], score(line[1], line[2], line[3]))
                conn.commit()
                entries += 1
            if entries in (0, 1):
                print(f"{entries} record was inserted into {db_name}")
            else:
                print(f"{entries} records were inserted into {db_name}")
        else:
            row = 0
            for line in file_reader:
                if row == 0:
                    row += 1
                else:
                    db_insertion(cur, line[0], line[1], line[2], line[3], score(line[1], line[2], line[3]))
                    conn.commit()
                    entries += 1
                    row += 1
            if entries in (0, 1):
                print(f"{entries} record was inserted into {db_name}")
            else:
                print(f"{entries} records were inserted into {db_name}")
    return db_name
