import sqlite3
import pandas as pd
import os
import datetime
import logging
#Add the logging stuff
def date_from_webkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return (epoch_start + delta)     
#master
class basic_db_parser:
    def __init__(self, db_name, table_name, db_location, db_parsed_path, log_path):
        self.db_name = db_name
        self.table_name = table_name
        self.db_location = db_location
        self.db_parsed_path = db_parsed_path
        self.log_path = log_path

    def exporting_table(self):
        
        logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(self.log_path),
            logging.StreamHandler()
            ]
        )

        root_directory = os.path.dirname(__file__)
        db_path = fr'{root_directory}\db_storage\{self.db_location}\{self.db_name}'
        db_exists = os.path.isfile(db_path)
  

        if db_exists == True:

            output_path = os.path.join(root_directory, 'parsed_outputs', self.db_parsed_path)
            os.makedirs(output_path, exist_ok=True)

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self.table_name}')
            rows = cursor.fetchall()

            df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
            os.makedirs(output_path, exist_ok=True)
            timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
            final_parsed_path = os.path.join(output_path,f'{self.table_name}_{timestamp}.csv')
            logging.info(f'Parsing {self.db_name}_{self.table_name}\n')
            df.to_csv(final_parsed_path, index=False)
            logging.info('Parsing Complete')
            conn.close()
            del df
            return final_parsed_path
            
        else:
            pass
            logging.info('Does not exist, moving to next database')  
#slave  
class chrome_csv(basic_db_parser):

    def exporting_table(self):
        csv_path = super().exporting_table()
        print(csv_path)
        
        if csv_path is None: 
            return
        
        logging.info(f'Loading {csv_path}')
        df = pd.read_csv(csv_path)
        logging.info('Converting time format')
        if "visit_time" in df.columns:
            logging.info(f'{csv_path}')
            df["visit_time"] = df["visit_time"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('Time conversion complete')
        
        if "last_visit_time" in df.columns:
            df["last_visit_time"] = df["last_visit_time"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('Time conversion complete')

        if "date_created" in df.columns:
            df["date_created"] = df["date_created"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('Time conversion complete')

        if "last_modified" in df.columns:
            df["last_modified"] = df["last_modified"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('Time conversion complete')

        return
#slave
   

def main():
    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'db_parser_{timestamp}.log' 
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers= [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
    )

    def export_chrome(db_name, db_tables, db_location, db_parsed_path, log_path):              
        for table in db_tables: 
            chrome = chrome_csv(db_name, table, db_location, db_parsed_path, log_path)
            chrome.exporting_table()
    logging.info('Exporting all databases')
    export_chrome('History', ['urls', 'visits'], 'chrome', 'Chrome History', log_file)

# Test if logging works


if __name__ == '__main__':
    main()