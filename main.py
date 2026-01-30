import shutil
import tkinter as tk
from tkinter import filedialog
import os
import datetime
import logging
import subprocess
import self_app_extraction
import sqlite3_parser
import xml_parser

#Mobile extraction path

 
###Collection phase###

def evidence_collection(gz_target, app_data_location, db_list, app_data_storage, log_path):
    app_item = self_app_extraction.database_grabber(gz_target, app_data_location, db_list, app_data_storage, log_path)
    app_item.app_datadata()


###Parsing Phase###


# Google Chrome
def export_chrome(db_name, db_tables, db_location, db_parsed_path, log_path):              
        for table in db_tables: 
            chrome = sqlite3_parser.chrome_csv(db_name, table, db_location, db_parsed_path, log_path)
            chrome.exporting_table() 
    
# Instagram

# Google Maps

# Opera Browser

# Twitter

# Whatsapp
def export_whatsapp(db_name, db_tables, db_location, db_parsed_path, log_path):
    for table in db_tables: 
        whatsapp = sqlite3_parser.basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
        whatsapp.exporting_table()
# Telegram

# Discord?

# Internet data, including DE
def export_xml(xml_name, xml_location, xml_parsed_path, log_path):
    xml_file = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
    xml_file.xml_to_csv()


def main():
    root = tk.Tk()
    root.withdraw()
    extraction_path = filedialog.askopenfilename()
    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'reiko_acquisition_{timestamp}.log'
    
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

    #Start Here Collection
    def all_collection():
        # Google Chrome 
        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
            db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
            app_data_storage='chrome',
            log_path=log_file, 
        )
        # Instagram
        # evidence_collection(
        #     gz_target=extraction_path,  
        #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        #     app_data_storage='chrome',
        #     log_path=log_file, 
        # )
        # Google Maps
        # evidence_collection(
        #     gz_target=extraction_path,  
        #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        #     app_data_storage='chrome',
        #     log_path=log_file, 
        # )
        # Opera Browser
        # evidence_collection(
        #     gz_target=extraction_path,  
        #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        #     app_data_storage='chrome',
        #     log_path=log_file, 
        # )
        # Twitter
        # evidence_collection(
        #     gz_target=extraction_path,  
        #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        #     app_data_storage='chrome',
        #     log_path=log_file, 
        # )
        # Whatsapp
        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/media/0/Android/media/com.whatsapp/WhatsApp', 
            db_list=['/msgstore.db.crypt14'], 
            app_data_storage='whatsapp',
            log_path=log_file, 
        )
        
        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/data/com.whatsapp/files', 
            db_list=['/key'], 
            app_data_storage='whatsapp',
            log_path=log_file, 
        )
        # Telegram
        # evidence_collection(
        #     gz_target=extraction_path,  
        #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        #     app_data_storage='chrome',
        #     log_path=log_file, 
        # )
        # Discord?
        # evidence_collection(
        #     gz_target=extraction_path,  
        #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        #     app_data_storage='chrome',
        #     log_path=log_file, 
        # )
        # Wifi/Internet data, including DE
        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/misc/bluedroid', 
            db_list=['/bt_config.bak', '/bt_config.conf', 'interop_database_dynamic.conf'], 
            app_data_storage='bluetooth',
            log_path=log_file, 
        )

        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/system', 
            db_list=['/netpolicy.xml'], 
            app_data_storage='wifi',
            log_path=log_file, 
        )
        
        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/misc/apexdata/com.android.wifi', 
            db_list=['/WifiConfigStore.xml', '/WifiConfigStoreSoftAp.xml'], 
            app_data_storage='wifi_std',
            log_path=log_file, 
        )

        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/misc_ce/0/apexdata/com.android.wifi', 
            db_list=['/WifiConfigStore.xml', '/WifiConfigStoreNetworkSuggestions.xml'], 
            app_data_storage='wifi_ce',
            log_path=log_file, 
        )

        evidence_collection(
            gz_target=extraction_path,  
            app_data_location=r'Dump/data/misc_de/0/apexdata/com.android.wifi', 
            db_list=['/WifiConfigStore.xml', '/WifiConfigStoreSoftAp.xml'], 
            app_data_storage='wifi_de',
            log_path=log_file, 
        )

    #Start Here Exporting
    def all_exporting():
        logging.info('[Exporting all databases]')
        # Google Chrome
        export_chrome('History', ['urls', 'visits'], 'chrome', 'Chrome History', log_file)
        export_chrome('Web Data', [], 'chrome', 'Chrome web_data', log_file)
        export_chrome('Top Sites', [], 'chrome', 'chrome Top_Sites', log_file)
        export_chrome('Cookies', [], 'chrome', 'Chrome Cookies', log_file)

        # Instagram

        # Google Maps

        # Opera Browser

        # Twitter

        # Whatsapp
        root_directory = os.path.dirname(__file__)
        wadb_path = fr'{root_directory}\db_storage\whatsapp'
        encrypted_wadb_exists = os.path.isfile(fr'{wadb_path}\msgstore.db.crypt14')
        if encrypted_wadb_exists == True: 
            execute_command(['wadecrypt.exe', fr'{wadb_path}\key', fr'{wadb_path}\msgstore.db.crypt14', fr'{wadb_path}\msgstore.db'])
            export_whatsapp('msgstore.db', ['message', 'jid'], 'whatsapp', 'whatsapp_chats', log_file)

        # Telegram

        # Discord?

        # Wifi/Internet, including DE
        logging.info('[Parsing XML Files]\n')
        export_xml(
            xml_name='WifiConfigStore.xml',
            xml_location='wifi', 
            xml_parsed_path='wifi',
            log_path=log_file,
        )
        logging.info('[All XML Files Parsed]')


    #Execution area
    
    #all_collection()
    all_exporting()

if __name__ == '__main__':
    main()
    # Cleanup
    root_directory = os.path.dirname(__file__)
    stored_db_path = os.path.join(root_directory, 'db_storage')
    parsed_path = os.path.join(root_directory, 'parsed_outputs')
    

    rm_folder = input('y or n for file deletion\n')
    if rm_folder == 'y':
        if os.path.exists(parsed_path): 
            shutil.rmtree(parsed_path)

        if os.path.exists(stored_db_path):
            shutil.rmtree(stored_db_path)
        # Figure out how to delete the folder without any errors
        print('Files were deleted\n')
        exit()
    else: 
         print('Files were not deleted and closing\n')
         exit()
