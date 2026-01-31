import gzip
import tarfile
import shutil
import tempfile
import os
import tkinter as tk
import datetime
from tkinter import filedialog
import posixpath

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
                        for filename in tar.getnames():
                            if filename.startswith(location) and filename.endswith(target_file):
                                print(f'[Extracting {files} to temp_dir loading area]')
                                os.makedirs('output', exist_ok=True)
                                tar.extract(filename, path='output')
                                with tempfile.TemporaryDirectory() as temp_dir:                                   
                                    try: 
                                        #Moves file from staging area to an output destination
                                        file_loading_area = os.path.join(temp_dir, target_file)
                                        final_path = os.path.join(stor_path, storage_name, target_file)                
                                        tar.extract(filename, path=temp_dir, filter="data")
                                        print(f'[Moving {target_file} to {final_path}]\n')
                                        shutil.move(file_loading_area, final_path)
                                    except Exception as e: 
                                        print(f'{e}')





file_extraction(
    gz_target= extraction_path, 
    evidence_files= kpi_evidence,
    #log_path= log_file
)
