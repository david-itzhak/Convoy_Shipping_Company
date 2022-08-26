def get_input_file_name() -> str:
    return str(input('Input file name \n'))


def check_is_file_ending(file_name: str, file_ending: str) -> bool:
    return True if file_name.endswith(file_ending) else False