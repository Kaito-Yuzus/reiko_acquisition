import tarfile
import os
import gzip
import shutil
import tempfile
from datetime import datetime

class database_grabber: 
    def __init__(self, gz_target, app_data_location, db_list, app_data_storage):
        self.gz_target = gz_target
        self.app_data_location = app_data_location
        self.db_list = db_list
        self.app_data_storage = app_data_storage

    def app_datadata(self):
        if not os.path.exists('reiko_acquisition\db_storage'):
            os.mkdir('reiko_acquisition\db_storage')
        output_path = os.path.join(r'reiko_acquisition\db_storage', self.app_data_storage)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        
        with gzip.open(self.gz_target) as gz_file:
            with tarfile.open(fileobj=gz_file) as tar:
                print('Files in tar archive:')
                for db in self.db_list:                 
                    for filename in tar.getnames():
                        if filename.startswith(self.app_data_location) and filename.endswith(db):
                            print(filename + '\nFILE EXISTS')
                            with tempfile.TemporaryDirectory() as temp_dir:
                                tar.extract(filename, path=temp_dir)
                                file_staging = os.path.join(temp_dir, filename)
                                shutil.move(file_staging, output_path)
                            

def main():

    def gather_chrome(gz_target, app_data_location, db_list, app_data_storage):
        chrome = database_grabber(gz_target, app_data_location, db_list, app_data_storage)
        chrome.app_datadata()   

    gz_target = r"C:\Users\Stinky\Desktop\output\extraction.tar.gz"

    gather_chrome(
            gz_target,  
            r'Dump/data/data/com.android.chrome/app_chrome/Default', 
            ['/History', '/Web Data'], 
            'chrome'          
                    )
    
if __name__ == '__main__':
    main()
