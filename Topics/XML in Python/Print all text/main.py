from lxml import etree

for element in etree.fromstring(input()):
    print(element.text)