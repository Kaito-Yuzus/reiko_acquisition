import gzip
import tarfile
import shutil
import tempfile
import os
import tkinter as tk
import datetime
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
extraction_path = filedialog.askopenfilename()
timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
log_file = f'reiko_acquisition_{timestamp}.log'
root_directory = os.path.dirname(__file__)
stor_path = os.path.join(root_directory, 'evidence_storage')

kpi_evidence = [
    
    #Chrome 
    (r'Dump/data/data/com.android.chrome/app_chrome/Default',
     ['History', 'Web Data', 'Top Sites', 'Cookies'],
     'chrome_browser'),
    
    #Network
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
]


def file_extraction(gz_target, evidence_files):

    if os.path.exists(stor_path) == False:
        os.mkdir(stor_path)

    print('[Opening Gzip Compressed File]\n')                
    with gzip.open(gz_target) as gz_file:
        with tarfile.open(fileobj=gz_file) as tar:
            print('[Opening Tar Archive]\n')                                   
            for location, files, storage_name in evidence_files: 
                if os.path.exists(os.path.join(stor_path, storage_name)) == False:
                    os.mkdir(os.path.join(stor_path, storage_name))
                    # Extracts files in a loading area
                    for target_file in files:
                        full_file_path = fr'{location}/{target_file}'
                        print(f'[Extracting {files} to temp_dir loading area]')
                        with tempfile.TemporaryDirectory() as temp_dir:                                   
                                #Moves file from staging area to an output destination
                                final_path = os.path.join(stor_path, storage_name, target_file)                
                                tar.extract(full_file_path, path=temp_dir)
                                print(f'[Moving {target_file} to {final_path}]\n')
                                shutil.move(fr'{temp_dir}\{target_file}', final_path)

                            





file_extraction(
    gz_target= extraction_path, 
    evidence_files= kpi_evidence,
    #log_path= log_file
)
