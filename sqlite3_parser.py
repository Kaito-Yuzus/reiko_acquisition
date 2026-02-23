import sqlite3
import pandas as pd
import os
import datetime
import logging
import subprocess

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
        db_path = fr'{root_directory}\evidence_storage\{self.db_location}\{self.db_name}'
        db_exists = os.path.isfile(db_path)
        
        if db_exists == True:

            output_path = os.path.join(root_directory, 'parsed_outputs', self.db_parsed_path)
            os.makedirs(output_path, exist_ok=True)

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self.table_name}')
            rows = cursor.fetchall()

            columns = []
            for column in cursor.description:
                columns.append(column[0])
            df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
            os.makedirs(output_path, exist_ok=True)
            timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
            final_parsed_path = os.path.join(output_path,f'{self.table_name}_{timestamp}.csv')
            logging.info(f'[Parsing {self.db_name}_{self.table_name}]')
            df.to_csv(final_parsed_path, index=False)
            logging.info('[Parsing Complete]\n')
            conn.close()
            del df
            return final_parsed_path
            
        else:
            pass
            logging.info('[Does not exist, moving to next database]')  
#slave  
class webrowser_csv(basic_db_parser):

    def exporting_table(self):
        csv_path = super().exporting_table()
        
        if csv_path is None: 
            return
        
        logging.info(f'[Loading {csv_path}]')
        df = pd.read_csv(csv_path)
        logging.info('[Converting time format]')
        if "visit_time" in df.columns:
            logging.info(f'[{csv_path}]')
            df["visit_time"] = df["visit_time"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')
        
        if "last_visit_time" in df.columns:
            df["last_visit_time"] = df["last_visit_time"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')

        if "date_created" in df.columns:
            df["date_created"] = df["date_created"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')

        if "last_modified" in df.columns:
            df["last_modified"] = df["last_modified"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')

        if "creation_utc" in df.columns:
            df["creation_utc"] = df["creation_utc"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')
        
        if "expires_utc" in df.columns:    
            df["expires_utc"] = df["expires_utc"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')

        if "last_access_utc" in df.columns:
            df["last_access_utc"] = df["last_access_utc"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')

        if "last_update_utc" in df.columns:
            df["last_update_utc"] = df["last_update_utc"].apply(date_from_webkit)
            df.to_csv(csv_path, index=False)
            logging.info('[Time conversion complete]')





        return
#slave
# class whatsapp_csv(basic_db_parser):
    #pass
   

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

    def execute_command(command):
            cmd_str = ' '.join(command)
            logging.info(f'Executing [{cmd_str}]')
            full_command = ["powershell", "-NoProfile", "-Command", cmd_str]

            process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                logging.info(line.strip())
            process.wait()
            logging.info(f'Command Complete')

    def export_chrome(db_name, db_tables, db_location, db_parsed_path, log_path):              
        for table in db_tables: 
            chrome = webrowser_csv(db_name, table, db_location, db_parsed_path, log_path)
            chrome.exporting_table()

    def export_whatsapp(db_name, db_tables, db_location, db_parsed_path, log_path):
        for table in db_tables: 
            whatsapp = basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
            whatsapp.exporting_table()


    logging.info('[Exporting all databases]')

    root_directory = os.path.dirname(__file__)
    # wadb_path = fr'{root_directory}\evidence_storage\whatsapp'
    # encrypted_wadb_exists = os.path.isfile(fr'{wadb_path}\msgstore.db.crypt14')
    # if encrypted_wadb_exists == True: 
    #     execute_command(['wadecrypt.exe', fr'{wadb_path}\key', fr'{wadb_path}\msgstore.db.crypt14', fr'{wadb_path}\msgstore.db'])
    #     export_whatsapp('msgstore.db', ['message', 'jid'], 'whatsapp', 'whatsapp_chats', log_file)

    # export_chrome('History', ['urls', 'visits'], 'chrome', 'Chrome History', log_file)

    def google_maps_export(db_name, db_tables, db_location, db_parsed_path, log_path): 
        for table in db_tables: 
            maps = basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
            maps.exporting_table()

    google_maps_evidence = [
    ('gnp_fcm_database',
        ['gnp_accounts'],
        'whatsapp',
        'whatsapp'), 

    ('Web gmm_storage.db',
        ['gmm_storage_table'],
        'whatsapp',
        'whatsapp'),         
    ]
    
    for database, tables, location, parsed_path in google_maps_evidence:
        google_maps_export(
            db_name = database,
            db_tables = tables,
            db_location = location,
            db_parsed_path = parsed_path,
            log_path = log_file
        )



if __name__ == '__main__':
    main()