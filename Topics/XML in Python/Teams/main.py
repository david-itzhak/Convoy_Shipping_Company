from lxml import etree

text_file = '.\data\dataset\input.txt'
root = etree.parse(text_file).getroot()
members = root[0]
for member in members:
    print(member.get('name'), end=' ')

