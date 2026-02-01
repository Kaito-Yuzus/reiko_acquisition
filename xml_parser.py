import os
import xml.etree.ElementTree as ET
import pandas as pd 
import datetime
import logging
#Remember to change evidence_storage to final path

timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
log_file = f'xml_parse{timestamp}.log'
#master
class basic_xml_parser: 
    def __init__(self, xml_name, xml_location, xml_parsed_path, log_path):
        self.xml_name = xml_name
        self.xml_location = xml_location
        self.xml_parsed_path = xml_parsed_path
        self.log_path = log_path

    def xml_to_csv(self):
        
        logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(self.log_path),
            logging.StreamHandler()
            ]
        )

        for xml_file in self.xml_name:
            root_directory = os.path.dirname(__file__)
            xml_path = os.path.join(root_directory, 'evidence_storage', self.xml_location, xml_file)
            xml_exists = os.path.isfile(xml_path)

            if xml_exists == True: 
                output_path = os.path.join(root_directory, 'parsed_outputs', self.xml_parsed_path)
                os.makedirs(output_path, exist_ok=True)
                tree = ET.parse(xml_path) 
                root = tree.getroot()
                data = []
                logging.info(f'[Parsing {self.xml_name}]')
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
                
                for column in ['Element', 'Name', 'Value']:
                        for i in range(len(df)):
                            cell_value = df.at[i, column]
                            if isinstance(cell_value, str):
                                df.at[i, column] = cell_value.strip()

                timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
                final_parsed_path = os.path.join(output_path,f'{xml_file}_{timestamp}.csv')
                logging.info(f'[Parsing Completed]')
                logging.info(f'[Exporting {self.xml_name} to CSV]\n')
                df.to_csv(final_parsed_path, index=False)
                del df
        return final_parsed_path


def main(): 

    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(log_file),
            logging.StreamHandler()
            ]
    )

    def export_xml(xml_name, xml_location, xml_parsed_path, log_path):
        xml_file = basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
        xml_file.xml_to_csv()
    
    logging.info('[Parsing XML Files]\n')

    export_xml(
        xml_name= ['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
        xml_location='wifi_std', 
        xml_parsed_path='wifi_std',
        log_path=log_file,
    )

    logging.info('[All XML Files Parsed]')
        



if __name__ == '__main__': 
    main()




