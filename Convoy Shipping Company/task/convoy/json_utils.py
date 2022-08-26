import json
from db_utils import fetch_rows_with_score_more_3_from_db


def create_json_file(db_name: str, table_name: str):
    json_file_name = db_name.replace('.s3db', '.json')
    table_dictionary, vehicle_count = get_table_dictionary_and_vehicle_count_score_more_3(db_name, table_name)
    generate_json_file(table_dictionary, json_file_name)
    print(f"{vehicle_count} vehicle{'s' if vehicle_count > 1 else ''} {'were' if vehicle_count > 1 else 'was'} saved into {json_file_name}")


def generate_json_file(table_dictionary, json_file_name: str):
    with open(json_file_name, 'w') as json_file:
        json.dump(table_dictionary, json_file)


def get_table_dictionary_and_vehicle_count_score_more_3(db_name: str, table_name: str) -> (dict, int):
    db_rows = fetch_rows_with_score_more_3_from_db(db_name, table_name)
    return {table_name: db_rows}, len(db_rows)