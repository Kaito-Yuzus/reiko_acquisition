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
     ['/History', '/Web Data', '/Top Sites', '/Cookies'],
     'chrome_browser'),
    
    
    
    
    
    
    
    
    
    #Network
    (r'Dump/data/misc/bluedroid',
     ['/bt_config.bak', '/bt_config.conf', 'interop_database_dynamic.conf'],
     'bluetooth'),

    (r'Dump/data/system',
     ['/netpolicy.xml'],
     'wifi'),

    (r'Dump/data/misc/apexdata/com.android.wifi',
     ['/WifiConfigStore.xml', '/WifiConfigStoreSoftAp.xml'],
     'wifi_std'),

    (r'Dump/data/misc_ce/0/apexdata/com.android.wifi',
     ['/WifiConfigStore.xml', '/WifiConfigStoreNetworkSuggestions.xml'],
     'wifi_ce'),
]

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
        full_command = ['powershell', '-NoProfile', '-Command', cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            logging.info(line.strip())
        process.wait()
        logging.info(f'Command Complete')

    #Start Here Collection

    def main_collection(gz_target, app_data_location, app_evidence_list, app_data_storage, log_path): 
        all_evidence = self_app_extraction.evidence_grabber(gz_target, app_data_location, app_evidence_list, app_data_storage, log_path)
        all_evidence.app_datadata()

    for location, files, storage_name in kpi_evidence:
        main_collection(
            gz_target = extraction_path,
            app_data_location = location,
            app_evidence_list = files,
            app_data_storage =  storage_name,
            log_path = log_file
            )
        



if __name__ == '__main__':
    main()
    # Cleanup
    root_directory = os.path.dirname(__file__)
    stored_db_path = os.path.join(root_directory, 'evidence_storage')
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
