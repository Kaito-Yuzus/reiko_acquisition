import gzip
import tarfile
import shutil
import os
import tkinter as tk
import datetime
from tkinter import filedialog
import logging
'''Fast file extraction from tar/gzip using full paths. Consider using getnamelist() if its a newphone
because I might not know the paths, but the names of the file I will know. Is very slow
Consider making a stored list of all the pathes/files when I make a universal plugin. 
'''

class evidence_grabber: 
    def __init__(self, gz_target, evidence_files, log_path):
        self.gz_target = gz_target
        self.evidence_files = evidence_files
        self.log_path = log_path
    
    def file_extraction(self):
        logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(self.log_path),
            logging.StreamHandler()
        ]
        )

        stor_path = os.path.join('./reiko_acquisition/', 'evidence_storage')

        if os.path.exists(stor_path) == False:
            os.mkdir(stor_path)

        with gzip.open(self.gz_target) as gz_file:
            logging.info('[Opening Gzip Compressed File]\n')

            with tarfile.open(fileobj=gz_file) as tar:
                logging.info('[Opening Tar Archive]\n')

                for location, files, storage_name in self.evidence_files: 
                

                    if files == ['all_dir']:
                        final_dest = os.path.join(stor_path, storage_name, 'all_dir')
                        os.makedirs(final_dest, exist_ok=True)
                        logging.info(f'[Extracting All Files From {location}]')
                        for member in tar.getmembers():
                            if member.isfile() and member.name.startswith(location):
                                file_name = os.path.basename(member.name)
                                final_dest_file = os.path.join(final_dest, file_name)
                                if os.path.exists(final_dest_file):
                                    logging.info(f'[{file_name} Already Exists]')
                                    continue

                                logging.info(f'[Extracting {member.name} to {final_dest}]')
                                tar.extract(member, path='tmp')
                                shutil.move(os.path.join('tmp', member.name), final_dest)

                    else: 
                        final_dest = os.path.join(stor_path, storage_name)
                        os.makedirs(final_dest, exist_ok=True)
                        for single in files:
                            final_dest_file = os.path.join(final_dest, single)
                            if os.path.exists(final_dest_file):
                                logging.info(f'[{single} Already Exists]')
                                continue

                            gtfile_path = f"{location}/{single}"
                            try:
                                tar.getmember(gtfile_path)

                            except:
                                logging.info(f'[{gtfile_path} Was Not Found, Skipping File]')
                                continue
                        
                            logging.info(f'[Extracting {single} From {location} To tmp Staging Area]')      
                            tar.extract(gtfile_path, path='tmp', filter="data")
                            fstaging = os.path.join('tmp', location, single)
                            logging.info(f'[Copying {single} to {final_dest}\n')
                            shutil.move(fstaging, final_dest)

        if os.path.exists(os.path.join('tmp')):
            logging.info('[Cleaning Staging Area]\n')
            shutil.rmtree(os.path.join('tmp'))

def main(): 

    kpi_evidence = [
    #Chrome 
    (r'Dump/data/data/com.android.chrome/app_chrome/Default',
    ['History', 'Web Data', 'Top Sites', 'Cookies'],
    'chrome_browser'),

    (r'Dump/data/misc/bluedroid',
    ['bt_config.bak', 'bt_config.conf', 'interop_database_dynamic.conf'],
    'bluetooth'),

    (r'Dump/data/system',
    ['netpolicy.xml'],
    'wifi'),

    (r'Dump/data/misc/apexdata/com.android.wifi',
    ['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
    'wifi_std'),

    (r'Dump/data/misc_ce/0/apexdata/com.android.wifi',
    ['WifiConfigStore.xml', 'WifiConfigStoreNetworkSuggestions.xml'],
    'wifi_ce'),

    (r'Dump/data/data/com.snapchat.android/databases',
    ['arroyo.db', 'main.db'],
    'snapchat'),

    (r'Dump/data/data/com.snapchat.android/shared_prefs',
    ['LoginSignupStore'],
    'snapchat'),

    # (r'Dump/data/data/com.snapchat.android/files/native_content_manager',
    #  ['all_dir'],
    #  'snapchat'),
]

    root = tk.Tk()
    root.withdraw()
    extraction_path = filedialog.askopenfilename()
    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'file_acquisition_{timestamp}.log'
    
    
    def main_collection(gz_target, evidence_files, log_path): 
        extract = evidence_grabber(gz_target, evidence_files, log_path)
        extract.file_extraction()

    main_collection(
        gz_target= extraction_path, 
        evidence_files= kpi_evidence,
        log_path= log_file
    )

if __name__ == '__main__': 
    main()    




