import defusedxml.ElementTree


class NfoReader:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path
        self.tree = defusedxml.ElementTree.parse(xml_file_path)
        self.root = self.tree.getroot()

    def get_element_value(self, element_path):
        element = self.root.find(element_path)
        return element.text if element is not None else None
