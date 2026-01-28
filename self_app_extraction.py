import tarfile
import os
import gzip
import shutil
import tempfile
import datetime
import logging
import tkinter as tk
from tkinter import filedialog

class database_grabber: 
    def __init__(self, gz_target, app_data_location, db_list, app_data_storage, log_path):
        self.gz_target = gz_target
        self.app_data_location = app_data_location
        self.db_list = db_list
        self.app_data_storage = app_data_storage
        self.log_path = log_path

    def app_datadata(self):
        logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(self.log_path),
            logging.StreamHandler()
            ]
        )

        if os.path.exists(r'reiko_acquisition\db_storage') == False:
            os.mkdir(r'reiko_acquisition\db_storage')
        output_path = os.path.join(r'reiko_acquisition\db_storage', self.app_data_storage)
        if os.path.exists(output_path) == False:
            os.mkdir(output_path) 
        
        with gzip.open(self.gz_target) as gz_file:
            with tarfile.open(fileobj=gz_file) as tar:
                logging.info('[Moving and Checking Files]')
                for db in self.db_list:                 
                    for filename in tar.getnames():
                        if filename.startswith(self.app_data_location) and filename.endswith(db):
                            logging.info(f'[Extracting {filename}]')
                            # Extracts files in a loading area
                            with tempfile.TemporaryDirectory() as temp_dir:
                                tar.extract(filename, path=temp_dir, filter="data")
                                file_staging = os.path.join(temp_dir, filename)
                                #Moves file from staging area to an output destination
                                shutil.move(file_staging, output_path)
                            
                            
def main():

    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'db_parsing_{timestamp}.log' 
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers= [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
    
    def gather_evidence(gz_target, app_data_location, db_list, app_data_storage, log_path):
        evidence = database_grabber(gz_target, app_data_location, db_list, app_data_storage, log_path)
        evidence.app_datadata()   

    root = tk.Tk()
    root.withdraw()
    extraction_path = filedialog.askopenfilename()

    gather_evidence(
        gz_target=extraction_path,  
        app_data_location=r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        db_list=['/History', '/Web Data'], 
        app_data_storage='chrome',
        log_path=log_file,        
    )
    
if __name__ == '__main__':
    main()
