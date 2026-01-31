kpi_evidence = [
    (r"Dump/data/misc/bluedroid",
     ["/bt_config.bak", "/bt_config.conf", "interop_database_dynamic.conf"],
     "bluetooth"),

    (r"Dump/data/system",
     ["/netpolicy.xml"],
     "wifi"),

    (r"Dump/data/misc/apexdata/com.android.wifi",
     ["/WifiConfigStore.xml", "/WifiConfigStoreSoftAp.xml"],
     "wifi_std"),

    (r"Dump/data/misc_ce/0/apexdata/com.android.wifi",
     ["/WifiConfigStore.xml", "/WifiConfigStoreNetworkSuggestions.xml"],
     "wifi_ce"),
]
extraction_path = 'extraction path'
log_file = 'log file'



log_path=log_file,
def printing(gz_target, app_data_location, app_evidence_list, app_data_storage, log_path): 
     print(gz_target)
     print(app_data_location)
     print(app_evidence_list)
     print(app_data_storage)
     print(f'{log_path}\n')

         
    


for location, files, storage_name in kpi_evidence:

    printing(
        gz_target=extraction_path,
        app_data_location=location,
        app_evidence_list=files,
        app_data_storage=storage_name,
        log_path=log_file,
    )
