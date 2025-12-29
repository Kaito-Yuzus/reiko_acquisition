import sqlite3
import pandas as pd
import os

def exporting_table(db_name, table_name):
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    root_directory = os.path.dirname(current_directory)
    db_path = f'{root_directory}/db_storage/{db_name}'
    db_exists = os.path.isfile(db_path)
    if db_exists == True:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        output = cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
        df.to_csv( f'{table_name}.csv', index=False)
        print('\n Complete')
    else: 
        print('\n Exiting')
        exit


exporting_table('Web Data', 'autofill')

