import os
###############################################################################
def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
###############################################################################   
dict_ = {}
import json
with open(os.path.join('name.json'), 'w') as fp:
    json.dump(dict_, fp)
fp.close()