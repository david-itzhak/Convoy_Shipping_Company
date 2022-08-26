from lxml import etree
from db_utils import fetch_rows_with_score_less_or_equal_3_from_db


def generate_xml_text(table_dictionary: dict) -> str:
    def create_vehicle_element(vehicle_entry):
        return f'''
                    <vehicle>
                        <vehicle_id>{vehicle_entry.get('vehicle_id')}</vehicle_id>
                        <engine_capacity>{vehicle_entry.get('engine_capacity')}</engine_capacity>
                        <fuel_consumption>{vehicle_entry.get('fuel_consumption')}</fuel_consumption>
                        <maximum_load>{vehicle_entry.get('maximum_load')}</maximum_load>
                    </vehicle>
                '''

    def create_convoy_element(vehicle_elements_list_: list) -> str:
        vehicles_element_text = "\n".join(vehicle_elements_list_)
        return f'''
                    <convoy>
                        {vehicles_element_text}
                    </convoy>
                '''

    def create_vehicle_elements_list(table_dictionary_: dict) -> list:
        vehicle_elements_list_: list = []
        vehicles_list: list = table_dictionary_.get('convoy')
        for vehicle in vehicles_list:
            vehicle_element = create_vehicle_element(vehicle)
            vehicle_elements_list_.append(vehicle_element)
        return vehicle_elements_list_

    vehicle_elements_list: list = create_vehicle_elements_list(table_dictionary)

    return create_convoy_element(vehicle_elements_list)


def write_xml_text_to_file(xml_text: str, xml_file_name: str):
    root = etree.fromstring(xml_text)
    tree = etree.ElementTree(root)
    tree.write(xml_file_name)


def get_table_dictionary_and_vehicle_count_score_less_or_equal_3(db_name: str, table_name: str) -> (dict, int):
    db_rows = fetch_rows_with_score_less_or_equal_3_from_db(db_name, table_name)
    return {table_name: db_rows}, len(db_rows)


def create_xml_file(db_name: str, table_name: str):
    xml_file_name = db_name.replace('.s3db', '.xml')
    table_dictionary, vehicle_count = get_table_dictionary_and_vehicle_count_score_less_or_equal_3(db_name, table_name)
    xml_text = generate_xml_text(table_dictionary)
    write_xml_text_to_file(xml_text, xml_file_name)
    print(f"{vehicle_count} vehicle{'s' if vehicle_count > 1  or vehicle_count == 0 else ''} {'were' if vehicle_count > 1 or vehicle_count == 0 else 'was'} saved into {xml_file_name}")
