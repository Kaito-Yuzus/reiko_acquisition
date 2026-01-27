import logging 
import subprocess

import datetime

timestamp = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
log_file = f'extraction_{timestamp}.log'

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers= [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def execute_command(command):
    cmd_str = ' '.join(command)
    logging.info(f'Executing [{cmd_str}]')
    full_command = ["powershell", "-NoProfile", "-Command", cmd_str]

    process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        logging.info(line.strip())
    process.wait()
    logging.info(f'Command Complete')



def main(): 
    execute_command(['ls'])
    removal_question = 'Would you like to delete the created path y or n'
    logging.info(removal_question)
    remove_leftovers  = input(f'{removal_question}\n')
    logging.info(remove_leftovers)

main()

