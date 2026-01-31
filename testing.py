kpi_evidence = [
    
    #Chrome 
    (r'Dump/data/data/com.android.chrome/app_chrome/Default',
     ['History', 'Web Data', 'Top Sites', 'Cookies'],
     'chrome_browser'),
    
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
]

for location, files, storage in kpi_evidence: 
    for file in files: 
        print(file)