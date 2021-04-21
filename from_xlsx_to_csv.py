#!/usr/bin/env python3

import pandas as pd


def from_xlsx_to_csv(file_path):
    """Return a csv file path given a xlsx file path"""

    my_df = pd.read_excel(file_path, sheet_name='Vehicles', dtype=str)
    to_file = file_path.replace('.xlsx', '.csv')
    my_df.to_csv(to_file, index=False)
    if my_df.shape[0] in (0, 1):
        print(f"{my_df.shape[0]} line was added to {to_file}")
    else:
        print(f"{my_df.shape[0]} lines were added to {to_file}")
    return to_file
