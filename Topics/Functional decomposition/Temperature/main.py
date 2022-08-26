def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    if unit.upper() == 'F':
        print(fahrenheit_to_celsius(float(temperature)), 'C')
    elif unit.upper() == 'C':
        print(celsius_to_fahrenheit(float(temperature)), 'F')
    else:
        print(f'{unit} - unsupported temperature unit')
