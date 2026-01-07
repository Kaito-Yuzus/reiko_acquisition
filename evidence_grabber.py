import tarfile
import zipfile
import os
import shutil
import tempfile
# Works for Windows
class database_grabber: 
    def __init__(self, archive_target, zp_target, app_data_location, db_list, app_data_storage):
        self.archive_target = archive_target
        self.zp_target = zp_target
        self.app_data_location = app_data_location
        self.db_list = db_list
        self.app_data_storage = app_data_storage

    def app_datadata(self):
        output_path = os.path.join(r'reiko_acquisition\db_storage', self.app_data_storage)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        with tarfile.open(self.archive_target, 'r') as tar:
            print('Opening Tar Archive')

            dump_zip = tar.extractfile(self.zp_target)

            with zipfile.ZipFile(dump_zip) as z: 
                all_files = z.namelist()
                for db in self.db_list:
                    for name in all_files:
                        if name.startswith(self.app_data_location) and name.endswith(db):
                            print(f'\n{name}')
                            print('File Exists')
                            with tempfile.TemporaryDirectory() as temp_dir:
                                file_staging = z.extract(name, path=temp_dir)
                                shutil.move(file_staging, output_path)
                                #Add a timestamp to the extracted file, so its always different





def main():

    def gather_chrome(archive_target, zp_target, app_data_location, db_list, app_data_storage):
        chrome = database_grabber(archive_target, zp_target, app_data_location, db_list, app_data_storage)
        chrome.app_datadata()   

    archive_target = r'C:\Users\Stinky\Desktop\forensic_tools\datasets\Android_14_Public_Image.tar\Android_14_Public_Image.tar' 
    zp_target = r'Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip'

    gather_chrome(
            archive_target, 
            zp_target, 
            r'Dump/data/data/com.android.chrome/app_chrome/Default', 
            ['/History', '/Web Data'], 
            'chrome'          
                    )
if __name__ == '__main__':
    main()