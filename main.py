import parser
from extras import evidence_grabber_dataset
import self_app_extraction
import shutil
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
extraction_path = filedialog.askopenfilename()

# archive_target = r'C:\Users\Stinky\Desktop\forensic_tools\datasets\Android_14_Public_Image.tar\Android_14_Public_Image.tar' 
# zp_target = r'Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip'

#gz_target = r"C:\Users\Stinky\Desktop\output\extraction.tar.gz"
 
gz_target = extraction_path

# # Google Chrome

# def gather_chrome_dataset(archive_target, zp_target, app_data_location, db_list, app_data_storage):
#     chrome = evidence_grabber_dataset.database_grabber(archive_target, zp_target, app_data_location, db_list, app_data_storage)
#     chrome.app_datadata()
    
def gather_chrome_gz(gz_target, app_data_location, db_list, app_data_storage):
        chrome = self_app_extraction.database_grabber
        (gz_target, app_data_location, db_list, app_data_storage)
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

    # gather_chrome_gz(
    #     gz_target,  
    #     r'Dump/data/data/com.android.chrome/app_chrome/Default', 
    #     ['/History', '/Web Data'], 
    #     'chrome'          
    #             )
    export_chrome('History', ['urls', 'visits'], 'chrome', 'Chrome History')
    export_chrome('Web Data', ['keywords', 'autofill'], 'chrome', 'Chrome Web Data')
    

if __name__ == '__main__':
    main()
    rm_folder = input('y or n for file deletion\n')
    if rm_folder == 'y':
        shutil.rmtree(r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\parsed_outputs')
        # Figure out how to delete the folder without any errors
        print('Files were deleted\n')
        exit()
    else: 
         print('Files were not deleted and closing\n')
         exit()
