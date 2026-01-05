import os

filename = os.path.basename(__file__)
output_path = os.path.join('reiko_acquisition/db_storage', filename, 'hello')
print(output_path)
