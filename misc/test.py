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

from tqdm import tqdm
a = 1
kpi_size = len(kpi_evidence)
with tqdm(total=kpi_size, desc="Main") as pbar:
    for item in kpi_evidence:
        pbar.update(1)
