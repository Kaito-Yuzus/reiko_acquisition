import sqlite3
import pandas as pd
import os
import datetime

transcript_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%f")


class basic_db_parser:
    def __init__(self, db_name, table_name, db_location, db_parsed_path):
        self.db_name = db_name
        self.table_name = table_name
        self.db_location = db_location
        self.db_parsed_path = db_parsed_path

    def exporting_table(self):
        
        root_directory = os.path.dirname(__file__)
        db_path = fr'{root_directory}\db_storage\{self.db_location}\{self.db_name}'
        
        db_exists = os.path.isfile(db_path)
  

        if db_exists == True:

            output_path = os.path.join(root_directory, 'parsed_outputs', self.db_parsed_path)
            os.makedirs(output_path, exist_ok=True)

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self.table_name}')
            rows = cursor.fetchall()

            df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
            os.makedirs(output_path, exist_ok=True)
            timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
            final_parsed_path = os.path.join(output_path,f'{self.table_name}_{timestamp}.csv')
            df.to_csv(final_parsed_path, index=False)
            conn.close()
            del df
            print(transcript_time)
            print(f'Exporting {self.db_name}\n')
            print(transcript_time)
            print('Parsing Complete\n')
            
        else:
            print('\n Does not exist, moving to next database')  
        
def main(): 
    pass 



if __name__ == '__main__':
    main()