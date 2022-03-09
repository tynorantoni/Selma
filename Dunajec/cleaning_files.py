from email import message
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)


import os
from support.log_module import write_log_custom



@write_log_custom('deleting')
def delete_file(filename):
    try:
        
        os.remove(filename)
    except FileNotFoundError as err:
        print(err)



delete_file('x')
