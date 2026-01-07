import datetime
import os

target = 'rename_me.txt'
ab_name = os.path.basename(target)
name_part, ext_part = os.path.splitext(ab_name)
timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
file_stamp = f"{name_part}_{timestamp}"


print(file_stamp)