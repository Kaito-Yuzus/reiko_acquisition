import sqlite3
import pandas as pd
import os
#gmm_storage.db
root = os.path.dirname(__file__)
file_path = os.path.join(root, "gmm_storage.db")
if os.path.isfile(file_path) == True:
    
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM gmm_storage_table  LIMIT 2')
            rows = cursor.fetchall()
            
            with open("output.txt", "w") as file:
                for row in rows:
                    file.write(row)

            


            # columns = []
            # for column in cursor.description:
            #     columns.append(column[0])
            # df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])
            
            
            conn.close()
            # del df
            
else:
    pass
    print("Ending")