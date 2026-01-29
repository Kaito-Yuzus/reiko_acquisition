import shutil
import tkinter as tk
from tkinter import filedialog
import os
import datetime
import logging
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
    
# Instagram

# Google Maps

# Opera Browser

# Twitter

# Whatsapp

# Telegram

# Discord?

# Internet data, including DE

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

    #Start Here

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
        db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
        app_data_storage='chrome',
        log_path=log_file, 
    )
    
    evidence_collection(
        gz_target=extraction_path,  
        app_data_location=r'Dump/data/data/com.whatsapp/files', 
        db_list=['/key'], 
        app_data_storage='chrome',
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
    # Internet data, including DE
    # evidence_collection(
    #     gz_target=extraction_path,  
    #     app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
    #     db_list=['/History', '/Web Data', '/Top Sites', '/Cookies'], 
    #     app_data_storage='chrome',
    #     log_path=log_file, 
    # )

    

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
