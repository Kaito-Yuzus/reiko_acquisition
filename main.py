import parser
import evidence_grabber
# import extraction_upload
# Location after extraction
archive_target = r'C:\Users\Stinky\Desktop\forensic_tools\datasets\Android_14_Public_Image.tar\Android_14_Public_Image.tar' 
zp_target = r'Android_14_Public_Image/UFED Google Pixel 7a 2024_07_28 (001)/EXTRACTION_FFS 01/EXTRACTION_FFS.zip'

# Google Chrome
def gather_chrome(archive_target, zp_target, app_data_location, db_list, app_data_storage):
    chrome = evidence_grabber.database_grabber(archive_target, zp_target, app_data_location, db_list, app_data_storage)
    chrome.app_datadata()
    
def export_chrome(app_db, db_tables, app_location):  
    for table in db_tables:
        chrome = parser.basic_db_parser(app_db, table, app_location)
        chrome.exporting_table()   

def export_opera(app_db, db_tables, app_location):           
    pass
# Instagram

# Google Maps

# Opera Browser

# Twitter

# Whatsapp

# Telegram

# Discord?

# Internet data, including DE

def main():
    gather_chrome(
        archive_target, 
        zp_target, 
        r'Dump/data/data/com.android.chrome/app_chrome/Default', 
        ['/History', '/Web Data'], 
        'chrome'          
                  )
    
    export_chrome('Web Data', ['keywords', 'autofill'], 'chrome')
    

if __name__ == '__main__':
    main()