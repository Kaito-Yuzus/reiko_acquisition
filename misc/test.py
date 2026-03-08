import os
import sys 
import subprocess


# Folder containing main.exe
base_dir = os.path.dirname(os.path.abspath(sys.executable))

# Path to your /bin/python.exe
python_exe = os.path.join(base_dir, r'poster_night\dist\bin\wadecrypt.exe')

# Optional: script you want to run
script_path = os.path.join(base_dir, "bin", "other_script.py")

# Run the external python

print(python_exe)