import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import logging
import datetime
import sys
#Works at the moment
def mobile_acquire():

    logger = logging.getLogger()

#Extraction Upload
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    extraction_path = filedialog.askdirectory()
    root.destroy()

    def execute_command(command):
        cmd_str = ' '.join(command)
        logger.info(f'Executing [{cmd_str}]')
        full_command = ["powershell", "-NoProfile", "-Command", cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            logger.info(line.strip())
        process.wait()
        logger.info(f'Command Complete')


    
    #Checks if program is an executable
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
        bin_dir = os.path.join(base_dir, '_internal', 'bin')
        adb_path = os.path.join(bin_dir, 'adb', 'adb.exe')
        script_location = os.path.join(bin_dir,'script.sh')
    else:
        adb_path = r'.\reiko_acquisition\bin\adb\adb.exe'
        script_location = r'reiko_acquisition\bin\script.sh'
    

    def check_device_connected():
        try:
            result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True)
            output = result.stdout.strip()
            lines = output.split('\n')
            devices = [line for line in lines[1:] if line.strip()]
            if devices:
                logger.info("Device(s) connected:")
                for device in devices:
                    logger.info(device.split()[0])  # Print the device ID
                return True
            else:
                print("No devices connected.")
                return False

        except FileNotFoundError:
            print("ADB is not installed or not in PATH.")
            return False

    if not check_device_connected():
        logger.info('Device not connected')
        print('Device not connected')
        pass

    if check_device_connected():
        logger.info('Device connected')
        print('Device connected')

        logger.info('Creating target directory')
        execute_command([adb_path, 'shell', "su -c mkdir /storage/emulated/0/target"])
        logger.info('Directory Created')
        execute_command([adb_path, 'shell', "su -c ls /storage/emulated/0"])
        logger.info('Sending Script')
        execute_command([adb_path, 'push', f"{script_location} /data/local/tmp/script.sh"])
        logger.info('Converting Script for Device')
        execute_command([adb_path, 'shell',  "su -c dos2unix /data/local/tmp/script.sh"])
        logger.info('Executing Script')
        execute_command([adb_path, 'shell', "su -c sh /data/local/tmp/script.sh"])
        logger.info('Script Finshed')
        logger.info('Transferring extraction to examiner machine')
        execute_command([adb_path, 'pull', f"sdcard/target/extraction.tar.gz {extraction_path}"])
        logger.info('Transfer complete')

        removal_question = 'Would you like to delete the created path y or n'
        logger.info(removal_question)
        remove_leftovers  = input(f'{removal_question}\n')
        logger.info(remove_leftovers)
        
        if remove_leftovers == 'y': 
            logger.info('Removing Leftovers')
            execute_command([adb_path, 'shell', "su -c rm -r /storage/emulated/0/target"])
            execute_command([adb_path, 'shell', "su -c rm /data/local/tmp/script.sh"])
        elif remove_leftovers == 'n': 
            pass

    else:
        ("No device connected.")
        
if __name__ == '__main__':
    mobile_acquire()


#Makes sure to convert bash script to unix format on transfer
