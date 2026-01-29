import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import logging
import datetime

#Works at the moment
def main():

#transcript
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

#Extraction Upload
    root = tk.Tk()
    root.withdraw()
    extraction_path = filedialog.askdirectory()
    root_directory = os.path.dirname(__file__)

    def execute_command(command):
        cmd_str = ' '.join(command)
        logging.info(f'Executing [{cmd_str}]')
        full_command = ["powershell", "-NoProfile", "-Command", cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            logging.info(line.strip())
        process.wait()
        logging.info(f'Command Complete')

    adb_path = r'.\reiko_acquisition\adb\adb.exe'
    script_location = os.path.join(root_directory, 'script.sh')

    logging.info('Creating target directory')
    execute_command([adb_path, 'shell', "su -c mkdir /storage/emulated/0/target"])
    logging.info('Directory Created')
    execute_command([adb_path, 'shell', "su -c ls /storage/emulated/0"])
    logging.info('Sending Script')
    execute_command([adb_path, 'push', f"{script_location} /data/local/tmp/script.sh"])
    logging.info('Executing Script')
    execute_command([adb_path, 'shell', "su -c sh /data/local/tmp/script.sh"])
    logging.info('Script Finshed')
    logging.info('Transferring extraction to examiner machine')
    execute_command([adb_path, 'pull', f"sdcard/target/extraction.tar.gz {extraction_path}"])
    logging.info('Transfer complete')

    removal_question = 'Would you like to delete the created path y or n'
    logging.info(removal_question)
    remove_leftovers  = input(f'{removal_question}\n')
    logging.info(remove_leftovers)
    
    if remove_leftovers == 'y': 
        logging.info('Removing Leftovers')
        execute_command([adb_path, 'shell', "su -c rm -r /storage/emulated/0/target"])
        execute_command([adb_path, 'shell', "su -c rm -r /data/local/tmp/script.sh"])
        exit
    elif remove_leftovers == 'n': 
        exit

if __name__ == '__main__':
    main()
