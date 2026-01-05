import tarfile
import zipfile
import os
import shutil

class database_grabber: 
    def __init__(self, archive_target, zp_target, evidence_location, db_list, evidence_storage):
        self.archive_target = archive_target
        self.zp_target = zp_target
        self.evidence_location = evidence_location
        self.db_list = db_list
        self.evidence_storage = evidence_storage

    def app_datadata(self):
        with tarfile.open(self.archive_target, 'r') as tar:
            print('Opening Tar Archive')
            dump_zip = tar.extractfile(self.zp_target)

            with zipfile.ZipFile(dump_zip) as z: 
                all_files = z.namelist()

                for db in self.db_list:
                    for name in all_files:
                        if name.startswith(self.evidence_location) and name.endswith(db):
                            print(f'\n{name}')
                            print('File Exists')
                            # filename = os.path.basename(name)
                            purgatory = z.extract(name, path='reiko_acquisition/purgatory')

                            # output_path = os.path.join('reiko_acquisition', filename)
                            shutil.move(purgatory, 'reiko_acquisition')

                            # reiko_acquisition
                        
                    

archive_target = '/mnt/c/Users/Stinky/Desktop/forensic_tools/datasets/Android_14_Public_Image.tar/Android_14_Public_Image.tar' 
zp_target = 'Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip'
evidence_location = 'Dump/data/data/com.android.chrome/app_chrome/Default'
db_target = ['/History', '/Web Data']
evidence_storage = 'chrome'
grab_chrome = database_grabber(archive_target, zp_target, evidence_location, ['/History', '/Web Data'], evidence_storage)
grab_chrome.app_datadata()