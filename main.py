from sql_parsing import parser


# Google Chrome
def export_chrome(app_db, db_tables, app_location):  
        for table in db_tables:
            chrome = parser.basic_db_parser(app_db, table, app_location)
            chrome.exporting_table()                
            



    
# Instagram

# Google Maps

# Opera Browser

# Twitter

# Whatsapp

# Telegram

# Discord?

# Internet data, including DE

def main():
    export_chrome('Web Data', ['keywords', 'autofill'], 'placeholder')
    

if __name__ == '__main__':
    main()