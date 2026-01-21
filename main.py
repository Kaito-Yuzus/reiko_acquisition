import parser
import self_app_extraction
import shutil
import tkinter as tk
import os
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
extraction_path = filedialog.askopenfilename()
 

#Google Chrome
    
def gather_chrome_gz(gz_target, app_data_location, db_list, app_data_storage):
        chrome = self_app_extraction.database_grabber(gz_target, app_data_location, db_list, app_data_storage)
        chrome.app_datadata()   

def export_chrome(db_name, db_tables, app_location, db_parsed_path):  
    for table in db_tables:
        chrome = parser.chrome_csv(db_name, table, app_location, db_parsed_path)
        chrome.exporting_table()   


# Instagram

# Google Maps

# Opera Browser

# Twitter

# Whatsapp

# Telegram

# Discord?

# Internet data, including DE

def main():

    gather_chrome_gz(
        extraction_path,  
        r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        ['/History', '/Web Data'], 
        'chrome'          
                )
    export_chrome('History', ['urls', 'visits'], 'chrome', 'Chrome History')
    export_chrome('Web Data', ['keywords', 'autofill'], 'chrome', 'Chrome Web Data')

    

if __name__ == '__main__':
    main()
    parsed_path = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\parsed_outputs'
    grabbed_db_path = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\db_storage'
    rm_folder = input('y or n for file deletion\n')
    if rm_folder == 'y':
        if os.path.exists(parsed_path): 
            shutil.rmtree(parsed_path)

        if os.path.exists(grabbed_db_path):
            shutil.rmtree(grabbed_db_path)
        # Figure out how to delete the folder without any errors
        print('Files were deleted\n')
        exit()
    else: 
         print('Files were not deleted and closing\n')
         exit()
