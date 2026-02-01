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

 
###Collection Items###
kpi_evidence = [
    #Chrome 
    (r'Dump/data/data/com.android.chrome/app_chrome/Default',
     ['History', 'Web Data', 'Top Sites', 'Cookies'],
     'chrome_browser'),

    #Discord
    (r'Dump/data/data/com.discord/shared_prefs',
     ['CacheStore.xml', 'ClientInfoCache.xml', 'FastCacheStore.xml'],
     'discord'),
     
     (r'Dump/data/data/com.discord/app_webview/Default',
     ['Cookies'],
     'discord'),

    #WhatsApp
    (r'Dump/data/media/0/Android/media/com.whatsapp/WhatsApp/Databases',
     ['msgstore.db.crypt14', 'msgstore-2024-07-22.1.db.crypt14', 'msgstore-2024-07-24.1.db.crypt14', 
      'msgstore-2024-07-25.1.db.crypt14', 'msgstore-2024-07-26.1.db.crypt14',
      'msgstore-increment-1.db.crypt14'],
     'whatsapp'),

     (r'Dump/data/data/com.whatsapp/files',
     ['key'],
     'whatsapp'),

    #Network
    (r'Dump/data/misc/bluedroid',
     ['bt_config.bak', 'bt_config.conf', 'interop_database_dynamic.conf'],
     'bluetooth'),

    (r'Dump/data/system',
     ['netpolicy.xml'],
     'wifi'),

    (r'Dump/data/misc/apexdata/com.android.wifi',
     ['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
     'wifi_std'),

    (r'Dump/data/misc_ce/0/apexdata/com.android.wifi',
     ['WifiConfigStore.xml', 'WifiConfigStoreNetworkSuggestions.xml'],
     'wifi_ce'),

     (r'Dump/data/misc_de/0/apexdata/com.android.wifi',
     ['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
     'wifi_de'),
]

def main():
    root = tk.Tk()
    root.withdraw()
    extraction_path = filedialog.askopenfilename()
    root_directory = os.path.dirname(__file__)
    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    transcript_path = os.path.join(root_directory, 'transcripts')
    os.makedirs(transcript_path, exist_ok=True)
    log_file = os.path.join(transcript_path, f'reiko_acquisition_{timestamp}.log')
    
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
        full_command = ['powershell', '-NoProfile', '-Command', cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            logging.info(line.strip())
        process.wait()
        logging.info(f'Command Complete')

    #Start Here Collection
    # def main_collection(gz_target, evidence_files, log_path): 
    #     all_evidence = self_app_extraction.evidence_grabber(gz_target, evidence_files, log_path)
    #     all_evidence.file_extraction()
    
    # logging.info(f'Collecting Evidence Files From {extraction_path}')
    # main_collection(
    #     gz_target = extraction_path,
    #     evidence_files = kpi_evidence,
    #     log_path = log_file
    #     )
    
    #Evidence To Parse
    chrome_browser_evidence = [
    #Chrome 
        ('History',
         ['urls', 'visits'],
         'chrome_browser',
         'chrome_browser'),

        ('Web Data',
         ['autofill', 'keywords', 'credit_cards', 'local_addresses', 'contact_info'],
         'chrome_browser',
         'chrome_browser'),

        ('Top Sites',
         ['top_sites'],
         'chrome_browser',
         'chrome_browser'),

        ('Cookies',
         ['cookies'],
         'chrome_browser',
         'chrome_browser')

    ]

    whatsapp_evidence = [
        ('msgstore.db.',
         ['message', 'jid'],
         'whatsapp',
         'whatsapp')

    ]


    internet_evidence = [
        
        (['WifiConfigStore.xml', 'WifiConfigStoreNetworkSuggestions.xml'],
         'wifi_ce',
         'wifi_ce'),
        
        # (['netpolicy.xml'],
        #  'wifi',
        #  'wifi'),
        #Add Later, is encoded as a AXML

         (['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
         'wifi_de',
         'wifi_de'),

         (['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
         'wifi_std',
         'wifi_std'),

         #Add Bluetooth later with custom csv input


    ]

    def chrome_export(db_name, db_tables, db_location, db_parsed_path, log_path): 
        for table in db_tables:
            chrome = sqlite3_parser.webrowser_csv(db_name, table, db_location, db_parsed_path, log_path)
            chrome.exporting_table()

    def whatsapp_export(db_name, db_tables, db_location, db_parsed_path, log_path):
        wadb_path = fr'{root_directory}\evidence_storage\whatsapp'
        encrypted_wadb_exists = os.path.isfile(fr'{wadb_path}\msgstore.db.crypt14')
        
        if os.path.isfile(os.path.join(wadb_path, 'msgstore.db')):
            logging.info("msgstore.db.crypt14 Is Already Decrypted")
        else:
            if encrypted_wadb_exists == True:
                logging.info("msgstore.db.crypt14 Is Being Decrypted") 
                execute_command(['wadecrypt.exe', fr'{wadb_path}\key', fr'{wadb_path}\msgstore.db.crypt14', fr'{wadb_path}\msgstore.db'])

        for table in db_tables:
            whatsapp = sqlite3_parser.basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
            whatsapp.exporting_table()

    def internet_export(xml_name, xml_location, xml_parsed_path, log_path):
        internet_files = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
        internet_files.xml_to_csv()

        
        
    
    #Start
    for database, tables, location, parsed_path in chrome_browser_evidence:
        chrome_export(
            db_name = database,
            db_tables = tables,
            db_location = location,
            db_parsed_path = parsed_path,
            log_path = log_file
        )
    
    for database, tables, location, parsed_path in whatsapp_evidence:
        whatsapp_export(
            db_name = database,
            db_tables = tables,
            db_location = location,
            db_parsed_path = parsed_path,
            log_path = log_file
        )

    
    for xml_file, location, parsed_path in internet_evidence: 
        internet_export(
            xml_name = xml_file,
            xml_location = location,
            xml_parsed_path= parsed_path, 
            log_path= log_file 
        )




if __name__ == '__main__':
    main()
    logging.info("Closing Transcript")

for handler in logging.getLogger().handlers[:]:
    handler.close()
    logging.getLogger().removeHandler(handler)

    # Cleanup
    root_directory = os.path.dirname(__file__)
    evidence_storage = os.path.join(root_directory, 'evidence_storage')
    transcript_path = os.path.join(root_directory, 'transcripts')
    parsed_path = os.path.join(root_directory, 'parsed_outputs')
    

    rm_folder = input('y or n for file deletion\n')
    if rm_folder == 'y':
        if os.path.exists(parsed_path): 
            shutil.rmtree(parsed_path)

        # if os.path.exists(evidence_storage):
        #     shutil.rmtree(evidence_storage)
        if os.path.exists(transcript_path): 
            shutil.rmtree(transcript_path)

        print('Files were deleted\n')
        exit()
    else: 
         print('Files were not deleted and closing\n')
         exit()
