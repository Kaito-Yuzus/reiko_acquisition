import parser
import self_app_extraction
import shutil
import tkinter as tk
from tkinter import filedialog
import os
import datetime
import logging

root = tk.Tk()
root.withdraw()
extraction_path = filedialog.askopenfilename()
 

#Google Chrome
    

# Instagram

# Google Maps

# Opera Browser

# Twitter

# Whatsapp

# Telegram

# Discord?

# Internet data, including DE

def main():

    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'extraction_{timestamp}.log'
    
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    #Start Here




    

if __name__ == '__main__':
    main()
    # Cleanup
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
