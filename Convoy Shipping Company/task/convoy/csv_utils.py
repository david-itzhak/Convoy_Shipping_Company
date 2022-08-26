import pandas as pd
import re
import csv

def xlsx_to_csv(file_name: str) -> str:
    csv_file_name: str = file_name.replace('.xlsx', '.csv')
    df = pd.read_excel(file_name, sheet_name='Vehicles', dtype=str)
    index_len: int = len(df.index)
    df.to_csv(csv_file_name, index=None, header=True)
    print(f"{index_len} line{'s' if index_len > 1 else ''} {'were' if index_len > 1 else 'was'} /"
          f"{'adedd' if index_len > 1 else 'added'} to {csv_file_name}")
    return csv_file_name


def check_csv_file(file_name: str) -> str:
    regex = re.compile(r'\d+')
    corrected_cells = 0
    output_file_name = file_name.replace('.csv', '[CHECKED].csv')
    with open(file_name, 'r') as input_csv_file, \
            open(output_file_name, 'w') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        output_csv_file.write(','.join(next(csv_reader)) + '\n')
        for row in csv_reader:
            for inx, item in enumerate(row):
                if not item.isnumeric():
                    row[inx] = regex.findall(item)[0]
                    corrected_cells += 1
            output_csv_file.write(','.join(row) + '\n')
    print(f"{corrected_cells} cell{'s' if corrected_cells > 1 else ''} {'were' if corrected_cells > 1 else 'was'} /"
          f"corrected in {output_file_name}")
    return output_file_name


def get_rows_from_csv(file_name: str) -> list:
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        rows = []
        for row in csv_reader:
            rows.append(row)
    return rows