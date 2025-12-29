import sqlite3
import pandas as pd
import os

def exporting_table(db_name, table_name):
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    root_directory = os.path.dirname(current_directory)
    db_path = f'{root_directory}/db_storage/{db_name}'
    db_exists = os.path.isfile(db_path)
    output_path = f'{root_directory}/parsed_outputs'
    if db_exists == True:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
        final_parsed_path = os.path.join(output_path,f'{table_name}.csv')
        df.to_csv(final_parsed_path, index=False)
        print('\n Complete')
    else: 
        print('\n Exiting')
        exit


exporting_table('Web Data', 'autofill')

