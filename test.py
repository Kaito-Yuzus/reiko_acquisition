import os

#Remember to change db_storage to final pat

class basic_xml_parser: 
    def __init__(self, xml_name, xml_location, xml_parsed_path):
        self.xml_name = xml_name
        self.xml_location = xml_location
        self.xml_parsed_path = xml_parsed_path

    def exporting_xml(self):
            
        root_directory = os.path.dirname(__file__)
        xml_path = fr'{root_directory}\db_storage\{self.xml_location}\{self.xml_name}'
        xml_exists = os.path.isfile(xml_path)



