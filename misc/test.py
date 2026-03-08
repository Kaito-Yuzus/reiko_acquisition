import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import logging
import datetime


import subprocess

adb_path = r'.\reiko_acquisition\bin\adb\adb.exe'

def device_connected():
    try:
        output = subprocess.check_output([adb_path, "devices"], text=True)
        return any("device" in line for line in output.splitlines()[1:])
    except FileNotFoundError:
        print("adb.exe not found")
        return False
    
if device_connected():
    print("A device is connected!")
else:
    print("No device connected.")