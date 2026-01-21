import subprocess
import os
import tkinter as tk
from tkinter import filedialog

def main():
    root = tk.Tk()
    root.withdraw()
    extraction_path = filedialog.askdirectory()
    root_directory = os.path.dirname(__file__)

    def execute_command(command):
        cmd_str = ' '.join(command)
        full_command = ["powershell", "-NoProfile", "-Command", cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')
        process.wait()

    adb_path = r'.\reiko_acquisition\adb\adb.exe'
    script_location = f'{root_directory}\script.sh'

    print('\nCreating target directory')
    execute_command([adb_path, 'shell', "su -c mkdir /storage/emulated/0/target"])
    print('\nDirectory Created')
    execute_command([adb_path, 'shell', "su -c ls /storage/emulated/0"])
    print('\nSending Script')
    execute_command([adb_path, 'push', f"{script_location} /data/local/tmp/script.sh"])
    print('\nExecuting Script')
    execute_command([adb_path, 'shell', "su -c sh /data/local/tmp/script.sh"])
    print('\nScript Finshed')
    print('Transferring extraction to examiner machine')
    execute_command([adb_path, 'pull', f"sdcard/target/extraction.tar.gz {extraction_path}"])
    print('Transfer complete')

    remove_leftovers  = input('Would you like to delete the created path y or n\n')
    if remove_leftovers == 'y': 
        execute_command([adb_path, 'shell', "su -c rm -r /storage/emulated/0/target"])
        execute_command([adb_path, 'shell', "su -c rm -r /data/local/tmp/script.sh"])
        exit
    elif remove_leftovers == 'n': 
        exit

if __name__ == '__main__':
    main()
