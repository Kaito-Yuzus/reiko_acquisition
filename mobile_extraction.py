import subprocess

def main():
    extraction_path = r'C:\Users\IKS.LAPTOP-AMM5L6TN\Desktop\output'

    def execute_command(command):
        # Run the command
        output = subprocess.run(command, capture_output=True, text=True)

        # Print the output
        print(output.stdout)
    terminal = 'powershell'
    adb_path = r'.\reiko_acquisition\adb\adb.exe'

    execute_command([terminal, adb_path, 'shell', "su -c mkdir /storage/emulated/0/target"])
    execute_command([terminal, adb_path, 'shell', "su -c ls /storage/emulated/0"])
    # execute_command([terminal, adb_path, 'shell', "su -c tar -czvf /storage/emulated/0/target/extraction.tar.gz data --transform 's|^|Dump/|S'"])
    execute_command([terminal, adb_path, 'pull', f"sdcard/target/hello.txt {extraction_path}"])
# sdcard/target/extraction.tar.gz
# Have a mechanism that checks if it work and to remove the created directory and the gzip tar file on target device
# This works, can proceed to using the gzip tar archive

if __name__ == '__main__':
    main()
