import sqlite3
from csv_utils import get_rows_from_csv


def execute_one_query(db_name: str, query: str):
    connection = sqlite3.connect(db_name)
    new_cursor = connection.cursor()
    new_cursor.execute(query)
    connection.close()


def create_table(db_name: str, table_name: str, columns_string: str):
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_string})'
    execute_one_query(db_name, query)


def insert_into_table_many(db_name: str, table_name: str, rows: list):
    conn = sqlite3.connect(db_name)
    cursor_name = conn.cursor()
    question_marks = ','.join(['?'] * len(rows[0]))
    cursor_name.executemany(f'INSERT INTO {table_name} VALUES ({question_marks})', rows)
    conn.commit()
    conn.close()
    rows_counter = len(rows)
    print(f"{rows_counter} record{'s' if rows_counter > 1 else ''} {'were' if rows_counter > 1 else 'was'} inserted into {db_name}")


def dict_factory(cursor, row) -> dict:
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def fetch_all_rows_from_db(db_name: str, table_name: str) -> list:
    connection = sqlite3.connect(db_name)
    connection.row_factory = dict_factory
    new_cursor = connection.cursor()
    new_cursor.execute(f'SELECT * FROM {table_name}')
    rows = new_cursor.fetchall()
    connection.close()
    return rows


def fetch_rows_with_score_more_3_from_db(db_name: str, table_name: str) -> list:
    connection = sqlite3.connect(db_name)
    connection.row_factory = dict_factory
    new_cursor = connection.cursor()
    new_cursor.execute(f'SELECT vehicle_id, engine_capacity, fuel_consumption, maximum_load FROM {table_name} WHERE score>3')
    rows = new_cursor.fetchall()
    connection.close()
    return rows


def fetch_rows_with_score_less_or_equal_3_from_db(db_name: str, table_name: str) -> list:
    connection = sqlite3.connect(db_name)
    connection.row_factory = dict_factory
    new_cursor = connection.cursor()
    new_cursor.execute(f'SELECT vehicle_id, engine_capacity, fuel_consumption, maximum_load FROM {table_name} WHERE score<=3')
    rows = new_cursor.fetchall()
    connection.close()
    return rows


def add_score_to_rows(rows: list):
    for row in rows:
        score = 0
        burned_fuel = 450 / 100 * int(row[2])
        pitstops_numbers = burned_fuel / int(row[1])
        if pitstops_numbers < 1:
            score += 2
        elif pitstops_numbers < 2:
            score += 1
        if burned_fuel <= 230:
            score += 2
        else:
            score += 1
        if int(row[3]) >= 20:
            score += 2
        row.append(str(score))


def create_and_populate_db(file_name: str) -> (str, str):
    db_name = file_name.replace('[CHECKED].csv', '.s3db')
    table_name = 'convoy'
    columns_string = '''
            vehicle_id INT PRIMARY KEY, 
            engine_capacity INT NOT NULL,
            fuel_consumption INT NOT NULL,
            maximum_load INT NOT NULL,
            score INT NOT NULL
        '''
    create_table(db_name, table_name, columns_string)
    rows = get_rows_from_csv(file_name)
    add_score_to_rows(rows)
    insert_into_table_many(db_name, table_name, rows)
    return db_name, table_name