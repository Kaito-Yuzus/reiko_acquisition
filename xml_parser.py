import os
import xml.etree.ElementTree as ET
import pandas as pd 
import datetime
#Remember to change db_storage to final path
#Also a write to host equivalent for transcripts
def transctipt(text): 
    RED = "\033[31m"
    RESET = "\033[0m"
    transcript_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%f")
    print(f'{RED}[{transcript_time}]{RESET}')
    print(f'{RED}[{text}]{RESET}\n')

#master
class basic_xml_parser: 
    def __init__(self, xml_name, xml_location, xml_parsed_path):
        self.xml_name = xml_name
        self.xml_location = xml_location
        self.xml_parsed_path = xml_parsed_path

    def xml_to_csv(self):
            
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
                    if value is not None: 
                        data.append({
                        'Element' : par_element.tag,
                        'Name': name,
                        'Value': value, 
                        })
                        # Strip whitespaces within the .csv for better use
                    elif num is not None:
                        data.append({
                        'Element' : par_element.tag,
                        'Name': name,
                        'Value': num, 
                        })
                    elif text is not None: 
                        data.append({
                        'Element' : par_element.tag,
                        'Name': name,
                        'Value': text, 
                        })
                    else: 
                        data.append({
                        'Element' : par_element.tag,
                        'Name': name,
                        'Value': 'Empty', 
                        })

            df = pd.DataFrame(data, columns=['Element', 'Name', 'Value'])
            timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
            final_parsed_path = os.path.join(output_path,f'{self.xml_name}_{timestamp}.csv')
            df.to_csv(final_parsed_path, index=False)
            del df
            return final_parsed_path


def main(): 
    def export_xml(xml_name, xml_location, xml_parsed_path):
        xml_file = basic_xml_parser(xml_name, xml_location, xml_parsed_path)
        xml_file.xml_to_csv()
    

    export_xml(
        xml_name='WifiConfigStore.xml',
        xml_location='wifi', 
        xml_parsed_path='wifi'
    )
        



if __name__ == '__main__': 
    main()




