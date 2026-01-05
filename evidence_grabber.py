import tarfile
import zipfile
import os
import shutil
import tempfile

class database_grabber: 
    def __init__(self, archive_target, zp_target, app_data_location, db_list, app_data_storage):
        self.archive_target = archive_target
        self.zp_target = zp_target
        self.app_data_location = app_data_location
        self.db_list = db_list
        self.app_data_storage = app_data_storage

    def app_datadata(self):
        output_path = os.path.join('reiko_acquisition/db_storage', self.app_data_storage)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        with tarfile.open(self.archive_target, 'r') as tar:
            print('Opening Tar Archive')
            dump_zip = tar.extractfile(self.zp_target)

            with zipfile.ZipFile(dump_zip) as z: 
                all_files = z.namelist()

                for db in self.db_list:
                    for name in all_files:
                        if name.startswith(self.app_data_location) and name.endswith(db):
                            print(f'\n{name}')
                            print('File Exists')
                            with tempfile.TemporaryDirectory() as temp_dir:
                                file_staging = z.extract(name, path=f'reiko_acquisition/{temp_dir}')
                                shutil.move(file_staging, output_path)
                            
