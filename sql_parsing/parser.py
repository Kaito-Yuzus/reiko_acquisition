import sqlite3
import pandas as pd
import os

def exporting_table(db_name, table_name):
    
    
    check = os.path.isdir(db_name)
    
    if check == True:
        conn = sqlite3.connect()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table_name}]')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
        df.to_csv('output.csv', index=False)
    else: 
        print('Exiting')
        exit


exporting_table('Login Data.db', 'reiko_acquisition/db_storage')
