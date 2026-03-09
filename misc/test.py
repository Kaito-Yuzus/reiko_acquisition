import os
import subprocess
import sys
import logging
import datetime


timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
log_file = f'mobile_extraction_{timestamp}.log'

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers= [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def execute_command(command):
        cmd_str = ' '.join(command)
        logging.info(f'Executing [{cmd_str}]')
        full_command = ["powershell", "-NoProfile", "-Command", cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            logging.info(line.strip())
        process.wait()
        logging.info(f'Command Complete')





base_dir = os.path.dirname(sys.executable)
bin_dir = os.path.join(base_dir, "bin")
exe_path = os.path.join(bin_dir,'wadecrypt.exe')
adb_path = os.path.join(bin_dir,'adb', 'adb.exe')

def check_device_connected():
    try:
        result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True)
        output = result.stdout.strip()
        lines = output.split('\n')
        devices = [line for line in lines[1:] if line.strip()]
        if devices:
            print("Device(s) connected:")
            for device in devices:
                print(device.split()[0])  # Print the device ID
            return True
        else:
            print("No devices connected.")
            return False

    except FileNotFoundError:
        print("ADB is not installed or not in PATH.")
        return False

if not check_device_connected():
    pass

if check_device_connected():
    pass

# execute_command([adb_path, 'shell', "su -c mkdir /storage/emulated/0/target"])
