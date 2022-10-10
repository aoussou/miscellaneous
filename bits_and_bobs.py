import os
###############################################################################
def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        
###############################################################################   
# SAVE A DICTIONARY
dict_ = {}
import json
with open(os.path.join('name.json'), 'w') as fp:
    json.dump(dict_, fp)
fp.close()

###############################################################################   
# GET LINES OF A TEXT FILE
def readText(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    f.close()
    
    return lines


###############################################################################   
# Access directory from home
from pathlib import Path
home_dir = Path.home()
home_path = os.fspath(home_dir)

full_dir_path = os.path.join(home_path, dir_path)
