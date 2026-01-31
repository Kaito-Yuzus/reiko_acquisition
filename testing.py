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
            for location, files, storage_name in evidence_files: 
                for single in files:      
                    gtfile_path = f"{location}/{single}"
                    extract_path = os.path.join('tmp', location)
                    os.makedirs(extract_path, exist_ok=True)
                    tar.extract(gtfile_path, path='tmp', filter="data")
                    final_dest = os.path.join(stor_path, storage_name)
                    os.makedirs(final_dest, exist_ok=True)
                    fstaging = os.path.join('tmp', location, single)
                    shutil.move(fstaging, final_dest)

file_extraction(
    gz_target= extraction_path, 
    evidence_files= kpi_evidence,
    #log_path= log_file
)
