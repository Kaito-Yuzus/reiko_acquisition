import os
import xml.etree.ElementTree as ET
import pandas as pd 

#Remember to change db_storage to final path

class basic_xml_parser: 
    def __init__(self, xml_name, xml_location, xml_parsed_path):
        self.xml_name = xml_name
        self.xml_location = xml_location
        self.xml_parsed_path = xml_parsed_path

    def exporting_xml(self):
            
        root_directory = os.path.dirname(__file__)
        xml_path = fr'{root_directory}\db_storage\{self.xml_location}\{self.xml_name}'
        xml_exists = os.path.isfile(xml_path)

        if xml_exists == True: 
            output_path = os.path.join(root_directory, 'parsed_outputs', self.xml_parsed_path)
            os.makedirs(output_path, exist_ok=True)
            tree = ET.parse(xml_path) 
            root = tree.getroot()
            data = []
            for par_element in root.iter():
                for item in par_element:
                    name = item.get('name')
                    value = item.get('value')
                    num = item.get('num')
                    text = item.text
                    if name is None: 
                        continue






def main(): 
    pass

if __name__ == '__main__': 
    pass




