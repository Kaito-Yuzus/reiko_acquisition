import tarfile
import zipfile
import os
# Make sure to update for Windows
#Current version is made for WSL
archive_target = '/mnt/c/Users/Stinky/Desktop/forensic_tools/datasets/Android_14_Public_Image.tar/Android_14_Public_Image.tar'
current_directory = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.dirname(current_directory)
db_location = 'chrome'
db_path = f'{root_directory}/db_storage/{db_location}'


#Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip
with tarfile.open(archive_target, 'r') as tar:
    print('Opening Tar Archive')

    dump_zip = tar.extractfile('Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip')
    with zipfile.ZipFile(dump_zip) as z: 
        with open('output.txt', 'a') as f:
            for file in z.namelist():
                if file.startswith('Dump/data/data/com.android.chrome/app_chrome/Default'):
                        f.write(f'\n{file}') 
            
        
        


    
