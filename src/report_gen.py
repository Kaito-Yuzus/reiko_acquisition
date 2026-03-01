

import os
from jinja2 import *

parent_folder = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\parsed_outputs'
stuff = os.walk(parent_folder)

# for root, adir, file  in stuff: 
#     print(f'{file}')
#     print(f'\n{os.path.basename(root)}')


titles = [
    'gaming', 
    'reading',
    'cooking'
]

env = Environment(loader=FileSystemLoader(r'reiko_acquisition\templates'))
template = env.get_template('report.html')

output = template.render(titles=titles)

with open('report_output.html', 'w') as f:
    f.write(output)

