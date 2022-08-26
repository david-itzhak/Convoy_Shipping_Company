from csv_utils import xlsx_to_csv, check_csv_file
from db_utils import create_and_populate_db
from json_utils import create_json_file
from xml_utils import create_xml_file
from commone_utils import get_input_file_name, check_is_file_ending


def main():
    file_name: str = get_input_file_name()
    if check_is_file_ending(file_name, '.xlsx'):
        file_name: str = xlsx_to_csv(file_name)
    if check_is_file_ending(file_name, '.csv') and not check_is_file_ending(file_name, '[CHECKED].csv'):
        file_name: str = check_csv_file(file_name)
    if not check_is_file_ending(file_name, '.s3db'):
        db_name, table_name = create_and_populate_db(file_name)
    else:
        db_name: str = file_name
        table_name: str = 'convoy'
    create_json_file(db_name, table_name)
    create_xml_file(db_name, table_name)


if __name__ == '__main__':
    main()
