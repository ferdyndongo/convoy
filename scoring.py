#!/usr/bin/env python3
import sqlite3


def scoring(file_path):
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    cur.execute('ALTER TABLE convoy ADD COLUMN score REAL;')
    conn.commit()
