import subprocess

def main():
    def execute_command(command):
        # Run the command
        output = subprocess.run(command, capture_output=True, text=True)

        # Print the output
        print(output.stdout)

    execute_command(['powershell', r'.\reiko_acquisition\adb\adb.exe', 'shell', 'su -c mkdir /sdcard/Dump'])
    execute_command(['powershell', r'.\reiko_acquisition\adb\adb.exe', 'shell', 'su -c ls /sdcard'])
    execute_command(['powershell', r'.\reiko_acquisition\adb\adb.exe', 'shell', 'su -c cp /data /storage/emulated/0/Dump'])
    execute_command(['powershell', r'.\reiko_acquisition\adb\adb.exe', 'shell', 'su -c ls /sdcard/Dump'])
if __name__ == '__main__':
    main()
