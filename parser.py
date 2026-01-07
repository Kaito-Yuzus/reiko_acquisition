import sqlite3
import pandas as pd
import os


class  basic_db_parser:
    def __init__(self, db_name, table_name, db_location):
        self.db_name = db_name
        self.table_name = table_name
        self.db_location = db_location

    def exporting_table(self):
        
        root_directory = os.path.dirname(__file__)
        db_path = fr'{root_directory}\db_storage\{self.db_location}\{self.db_name}'
        
        db_exists = os.path.isfile(db_path)
        output_path = os.path.join(root_directory, 'parsed_outputs')
        os.makedirs(output_path, exist_ok=True)

        if db_exists == True:

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self.table_name}')
            rows = cursor.fetchall()

            df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
            final_parsed_path = os.path.join(output_path,f'{self.table_name}.csv')
            df.to_csv(final_parsed_path, index=False)

            print('\n Complete')
        
        else:

            print('\n Exiting')
            exit

def main(): 
    pass 


if __name__ == '__main__':
    main()