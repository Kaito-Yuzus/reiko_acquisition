import tarfile
import zipfile
import os

class database_grabber: 
    def __init__(self, archive_target, zp_target, evidence_location):
        self.archive_target = archive_target
        self.zp_target = zp_target
        self.evidence_location = evidence_location

    def app_datadata(self):
        with tarfile.open(self.archive_target, 'r') as tar:
            print('Opening Tar Archive')
            dump_zip = tar.extractfile(self.zp_target)
            with zipfile.ZipFile(dump_zip) as z: 
                with open('output.txt', 'a') as f:
                    for file in z.namelist():
                        if file.startswith(self.evidence_location):
                                f.write(f'\n{file}') 
                    print('Complete')
            
t_target = '/mnt/c/Users/Stinky/Desktop/forensic_tools/datasets/Android_14_Public_Image.tar/Android_14_Public_Image.tar' 
z_target = 'Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip'
app_location = 'Dump/data/data/com.android.chrome/app_chrome/Default'
grab_chrome = database_grabber(t_target, z_target, app_location)
grab_chrome.app_datadata()