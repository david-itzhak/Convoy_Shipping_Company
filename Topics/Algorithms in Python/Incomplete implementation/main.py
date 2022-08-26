from string import ascii_uppercase


def startswith_capital_counter(names):
    return sum(1 for name in names if name[0] in ascii_uppercase)
