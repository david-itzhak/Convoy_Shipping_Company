from lxml import etree


def find_password(xml_string):

    def traverse_element(element):
        result = element.get('password')
        if result:
            return result
        else:
            for child in element:
                result = traverse_element(child)
                if result:
                    return result
        return None

    root = etree.fromstring(xml_string)
    return traverse_element(root)
