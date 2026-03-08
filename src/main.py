import shutil
import tkinter as tk
import os
import datetime
import logging
import subprocess
import self_app_extraction
import sqlite3_parser
import xml_parser
from tqdm import tqdm
import mobile_extraction
import report_gen
import sys 



banner_logo = r'''
   ___      _ __            ___                _     _ __  _         
  / _ \___ (_) /_____      / _ |_______ ___ __(_)__ (_) /_(_)__  ___ 
 / , _/ -_) /  '_/ _ \    / __ / __/ _ `/ // / (_-</ / __/ / _ \/ _ \
/_/|_|\__/_/_/\_\\___/   /_/ |_\__/\_, /\_,_/_/___/_/\__/_/\___/_//_/
                                    /_/                              
'''

###Collection Items###
kpi_evidence = [
    #Chrome 
    (r'Dump/data/data/com.android.chrome/app_chrome/Default',
    ['History', 'Web Data', 'Top Sites', 'Cookies'],
    'chrome_browser'),

    #Google Maps
    (r'Dump/data/data/com.google.android.apps.maps/databases',
    ['gnp_fcm_database', 'gmm_storage.db'],
    'google_maps'),

    (r'Dump/data/data/com.google.android.apps.maps/cache/image_manager_disk_cache',
    ['all_dir'],
    'google_maps'),

    #Discord
    (r'Dump/data/data/com.discord/shared_prefs',
    ['CacheStore.xml', 'ClientInfoCache.xml', 'FastCacheStore.xml'],
    'discord'),
    
    (r'Dump/data/data/com.discord/app_webview/Default',
    ['Cookies'],
    'discord'), 

    #WhatsApp
    (r'Dump/data/media/0/Android/media/com.whatsapp/WhatsApp/Databases',
    ['msgstore.db.crypt14', 'msgstore-2024-07-22.1.db.crypt14', 'msgstore-2024-07-24.1.db.crypt14', 
    'msgstore-2024-07-25.1.db.crypt14', 'msgstore-2024-07-26.1.db.crypt14',
    'msgstore-increment-1.db.crypt14'],
    'whatsapp'),

    (r'Dump/data/data/com.whatsapp/files',
    ['key'],
    'whatsapp'),

    #Network
    (r'Dump/data/misc/bluedroid',
    ['bt_config.bak', 'bt_config.conf', 'interop_database_dynamic.conf'],
    'bluetooth'),

    (r'Dump/data/system',
    ['netpolicy.xml'],
    'wifi'),

    (r'Dump/data/misc/apexdata/com.android.wifi',
    ['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
    'wifi_std'),

    (r'Dump/data/misc_ce/0/apexdata/com.android.wifi',
    ['WifiConfigStore.xml', 'WifiConfigStoreNetworkSuggestions.xml'],
    'wifi_ce'),

    (r'Dump/data/misc_de/0/apexdata/com.android.wifi',
    ['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
    'wifi_de'),

    #Telegram
    (r'Dump/data/data/org.telegram.messenger/files',
    ['file_to_path.db', 'cache4.db'],
    'telegram'),
    
    (r'Dump/data/data/org.telegram.messenger/shared_prefs',
    ['userconfing.xml'],
    'telegram'),

    #Snapchat
    (r'Dump/data/data/com.snapchat.android/databases',
    ['arroyo.db', 'main.db'],
    'snapchat'),

    (r'Dump/data/data/com.snapchat.android/shared_prefs',
    ['LoginSignupStore.xml'],
    'snapchat'),
    #Broken, need to fix
    # (r'Dump/data/data/com.snapchat.android/files/native_content_manager/com.snap.file_manager',
    # ['all_dir'],
    # 'snapchat'),

    #Mobile Device Info
    (r'Dump/data/system/users/0',
    #This needs AXML
    ['settings_secure.xml'],
    'device_info'),

    (r'Dump/data/system/usagestats/0',
    ['version'],
    'device_info'),

    (r'Dump/data/drm/pvt',
    ['ahrh'],
    'device_info'),

    (r'Dump/data/user_de/0/com.android.providers.telephony/databases',
    ['telephony.db'],
    'device_info'),

    (r'Dump/data/misc/bootstat',
    ['factory_reset', 'last_boot_time_utc'],
    'device_info'),

    (r'Dump/data/data/com.google.android.apps.turbo/databases',
    ['turbo.db', 'appusage.db'],
    'device_info'),

    (r'Dump/data/data/com.google.android.settings.intelligence/databases',
    ['battery-usage-db-v4'],
    'device_info'),




]

def main():
    timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    transcript_path = os.path.join('reiko_acquisition', 'transcripts')
    os.makedirs(transcript_path, exist_ok=True)
    log_file = os.path.join(transcript_path, f'reiko_acquisition_{timestamp}.log')
    
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers= [
            logging.FileHandler(log_file),
            #logging.StreamHandler()
        ]
    )
    def execute_command(command):
        cmd_str = ' '.join(command)
        logging.info(f'Executing [{cmd_str}]')
        full_command = ['powershell', '-NoProfile', '-Command', cmd_str]

        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            logging.info(line.strip())
        process.wait()
        logging.info(f'Command Complete')

    # Start Here Collection
    def main_collection(gz_target, evidence_files, log_path): 
        all_evidence = self_app_extraction.evidence_grabber(gz_target, evidence_files, log_path)
        all_evidence.file_extraction()
    

    
    #Evidence To Parse
    # Note to self, blobs will not get exported via csv

    #Sqlite stuff

    snapchat_evidence_sql = [
        #Has blobs and weirds files also
        ('arroyo.db',
        ['conversation', 'local_message_content'],
        'snapchat',
        'snapchat'),

        ('main.db',
        ['contact', 'story', 'friend'],
        'snapchat',
        'snapchat'),

    ]
    
    discord_evidence_sql = [
        ('Cookies',
        ['cookies'],
        'discord',
        'discord')

    ]

    chrome_browser_evidence_sql = [
        ('History',
        ['urls', 'visits'],
        'chrome_browser',
        'chrome_browser'),

        ('Web Data',
        ['autofill', 'keywords', 'credit_cards', 'contact_info'],
        'chrome_browser',
        'chrome_browser'),

        ('Top Sites',
        ['top_sites'],
        'chrome_browser',
        'chrome_browser'),

        ('Cookies',
        ['cookies'],
        'chrome_browser',
        'chrome_browser')

    ]

    google_maps_evidence_sql = [
        #Change db used and grab the rest, they are needed to be viewed
        ('gnp_fcm_database',
        ['gnp_accounts'],
        'google_maps',
        'google_maps'), 

        ('Web gmm_storage.db',
        ['gmm_storage_table'],
        'google_maps',
        'google_maps'),         
    ]
    
    
    
    whatsapp_evidence_sql = [
        ('msgstore.db.',
        ['message', 'jid'],
        'whatsapp',
        'whatsapp')

    ]

    device_info__evidence_sql = [
        ('turbo.db.',
        ['battery_event', 'charging_places'],
        'device_info',
        'device_info'),

        ('telephony.db.',
        ['carriers', 'siminfo'],
        'device_info',
        'device_info')

    ]



    #Xml stuff

    # device_info__evidence_xml = [
    #     #Requires AXML parsing
    #     (['settings_secure.xml'],
    #      'device_info',
    #      'device_info'),

    # ]

    discord_evidence_xml = [
        (['CacheStore.xml', 'ClientInfoCache.xml', 'FastCacheStore.xml'],
        'discord',
        'discord'),

    ]

    telegram_evidence_xml = [
        (['userconfing.xml'],
        'telegram',
        'telegram'),

    ]

    snapchat_evidence_xml = [
        (['LoginSignupStore.xml'],
        'snapchat',
        'snapchat'),
    ]

    internet_evidence_xml = [
        
        (['WifiConfigStore.xml', 'WifiConfigStoreNetworkSuggestions.xml'],
        'wifi_ce',
        'wifi_ce'),
        
        # (['netpolicy.xml'],
        #  'wifi',
        #  'wifi'),
        #Add Later, is encoded as a AXML

        (['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
        'wifi_de',
        'wifi_de'),

        (['WifiConfigStore.xml', 'WifiConfigStoreSoftAp.xml'],
        'wifi_std',
        'wifi_std'),

        #Add Bluetooth later with custom csv input
    ]

    
    
    #Start Export


############################################ SQLite ############################################

    def evidence_parsing():
        with tqdm(total=8, desc="Main") as pbar:
            #Chrome
            def chrome_export_sql(db_name, db_tables, db_location, db_parsed_path, log_path): 
                for table in db_tables:
                    chrome = sqlite3_parser.webrowser_csv(db_name, table, db_location, db_parsed_path, log_path)
                    chrome.exporting_table()

            for database, tables, location, parsed_path in chrome_browser_evidence_sql:
                chrome_export_sql(
                    db_name = database,
                    db_tables = tables,
                    db_location = location,
                    db_parsed_path = parsed_path,
                    log_path = log_file
                )
            pbar.update(1)

            #Device_info
            def device_info_export_sql(db_name, db_tables, db_location, db_parsed_path, log_path): 
                for table in db_tables:
                    device_info = sqlite3_parser.basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
                    device_info.exporting_table()

            for database, tables, location, parsed_path in device_info__evidence_sql:
                device_info_export_sql(
                    db_name = database,
                    db_tables = tables,
                    db_location = location,
                    db_parsed_path = parsed_path,
                    log_path = log_file
                )
                pbar.update(1)

            #Whatsapp
            def whatsapp_export_sql(db_name, db_tables, db_location, db_parsed_path, log_path):
                    base_dir = os.path.dirname(os.path.abspath(sys.executable))
                    python_exe = os.path.join(base_dir, r'bin\wadecrypt.exe')
                    wadb_path = os.path.join('reiko_acquisition', 'evidence_storage', 'whatsapp')
                    encrypted_wadb_exists = os.path.isfile(fr'{wadb_path}\msgstore.db.crypt14')
                    
                    if os.path.isfile(os.path.join(wadb_path, 'msgstore.db')):
                        logging.info("msgstore.db.crypt14 Is Already Decrypted")
                    else:
                        if encrypted_wadb_exists == True:
                            logging.info("msgstore.db.crypt14 Is Being Decrypted") 
                            execute_command([python_exe, fr'{wadb_path}\key', fr'{wadb_path}\msgstore.db.crypt14', fr'{wadb_path}\msgstore.db'])

                    for table in db_tables:
                        whatsapp = sqlite3_parser.basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
                        whatsapp.exporting_table()
            
            for database, tables, location, parsed_path in whatsapp_evidence_sql:
                whatsapp_export_sql(
                    db_name = database,
                    db_tables = tables,
                    db_location = location,
                    db_parsed_path = parsed_path,
                    log_path = log_file
                )
                pbar.update(1)

            #Discord
            def discord_export_sql(db_name, db_tables, db_location, db_parsed_path, log_path): 
                for table in db_tables:
                    discord = sqlite3_parser.basic_db_parser(db_name, table, db_location, db_parsed_path, log_path)
                    discord.exporting_table()

            for database, tables, location, parsed_path in discord_evidence_sql:
                discord_export_sql(
                    db_name = database,
                    db_tables = tables,
                    db_location = location,
                    db_parsed_path = parsed_path,
                    log_path = log_file
                )
                pbar.update(1)


        ############################################ XML ############################################

            #Internet
            def internet_export_xml(xml_name, xml_location, xml_parsed_path, log_path):
                internet_files = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
                internet_files.xml_to_csv()

            for xml_file, location, parsed_path in internet_evidence_xml: 
                internet_export_xml(
                    xml_name = xml_file,
                    xml_location = location,
                    xml_parsed_path= parsed_path, 
                    log_path= log_file 
                )
                pbar.update(1)

            #Telegram
            def telegram_export_xml(xml_name, xml_location, xml_parsed_path, log_path):
                telegram = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
                telegram.xml_to_csv()

            for xml_file, location, parsed_path in telegram_evidence_xml: 
                telegram_export_xml(
                    xml_name = xml_file,
                    xml_location = location,
                    xml_parsed_path= parsed_path, 
                    log_path= log_file 
                )
                pbar.update(1)

            #Discord
            def discord_export_xml(xml_name, xml_location, xml_parsed_path, log_path):
                discord = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
                discord.xml_to_csv()

            for xml_file, location, parsed_path in discord_evidence_xml: 
                discord_export_xml(
                    xml_name = xml_file,
                    xml_location = location,
                    xml_parsed_path= parsed_path, 
                    log_path= log_file 
                )
                pbar.update(1)

            #Snapchat
            def snapchat_export_xml(xml_name, xml_location, xml_parsed_path, log_path):
                snapchat = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
                snapchat.xml_to_csv()

            for xml_file, location, parsed_path in snapchat_evidence_xml: 
                snapchat_export_xml(
                    xml_name = xml_file,
                    xml_location = location,
                    xml_parsed_path= parsed_path, 
                    log_path= log_file 
                )
                pbar.update(1)

            #Device_info
            # def device_info_xml(xml_name, xml_location, xml_parsed_path, log_path):
            #     Device_info = xml_parser.basic_xml_parser(xml_name, xml_location, xml_parsed_path, log_path)
            #     Device_info.xml_to_csv()

            # for xml_file, location, parsed_path in device_info__evidence_xml: 
            #     device_info_xml(
            #         xml_name = xml_file,
            #         xml_location = location,
            #         xml_parsed_path= parsed_path, 
            #         log_path= log_file 
            #     )
            # pbar.update(1)


    ### Home Screen ###
    while True:
        menu_text = '''
        1. Acquire Rooted Mobile Device
        2. Extract Files from Created Dataset
        3. Parse All Collected Files from Extracted Files
        4. Render Interactive HTML Flask Report
        5. Exit Program
        '''

        print(banner_logo)
        print(menu_text)
        choice = input('Choose from the following options\n')
        
        if choice == '1':
            print('Option 1 Selected')
            acquire_warning = input('This can take a while, are you sure? y or n\n')
            if acquire_warning == 'y':
                mobile_extraction.mobile_acquire()
                if os.name == 'nt':
                    os.system('cls')
            else: 
                if os.name == 'nt':
                    os.system('cls')
                continue


        elif choice == '2':
            print('Option 2 Selected')
            from tkinter import filedialog
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            extraction_path = filedialog.askopenfilename()
            root.destroy()
            logging.info(f'Collecting Evidence Files From {extraction_path}')
            main_collection(
                gz_target = extraction_path,
                evidence_files = kpi_evidence,
                log_path = log_file
            )
            if os.name == 'nt':
                os.system('cls')


        elif choice == '3':
            print('Option 3 Selected')
            evidence_parsing()
            if os.name == 'nt':
                os.system('cls')

        elif choice == '4':        
            print('Rendering Report')
            report_gen.rend_report()
            if os.name == 'nt':
                os.system('cls')


        elif choice == '5':
            print('Exiting Program')
            logging.info("Closing Transcript")
            for handler in logging.getLogger().handlers[:]:
                handler.close()
                logging.getLogger().removeHandler(handler)

                # Cleanup
                evidence_storage = os.path.join('reiko_acquisition', 'evidence_storage')
                transcript_path = os.path.join('reiko_acquisition', 'transcripts')
                parsed_path = os.path.join('reiko_acquisition', 'parsed_outputs')
                
                rm_folder = input('Remove transcripts and parsed files? y or n\n')
                if rm_folder == 'y':
                    if os.path.exists(parsed_path): 
                        shutil.rmtree(parsed_path)
                    # if os.path.exists(evidence_storage):
                    #     shutil.rmtree(evidence_storage)
                    if os.path.exists(transcript_path): 
                        shutil.rmtree(transcript_path)
                    print('Files were deleted\n')
                    sys.exit()
                else: 
                    print('Files were not deleted and closing\n')
                    sys.exit()
        else: 
            print('Choose a valid input')
            if os.name == 'nt':
                os.system('cls')
        






if __name__ == '__main__':
    main()

