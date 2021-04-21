#!/usr/bin/env python 3
import pandas as pd


def pre_process(file_path):
    """return the path for the cleaned csv file given a path of a raw csv in input."""

    my_df = pd.read_csv(file_path, dtype=str)
    count = 0
    for column in my_df.columns:
        for i in range(len(my_df[column].values)):
            if not my_df[column].values[i].isdigit():
                count += 1
                items = my_df[column].values[i].split()
                if len(items) == 1:
                    cell = []
                    for item in items[0]:
                        if item.isdigit():
                            cell.append(item)
                    my_df[column].values[i] = "".join(cell)
                elif len(items) > 1:
                    for item in items:
                        if item.isdigit():
                            my_df[column].values[i] = item
    checked_file = file_path.replace('.csv', '[CHECKED]' + '.csv')
    my_df.to_csv(checked_file, header=False, index=False)
    if count in (0, 1):
        print(f'{count} cell was corrected in {checked_file}')
    else:
        print(f'{count} cells were corrected in {checked_file}')
    return checked_file
