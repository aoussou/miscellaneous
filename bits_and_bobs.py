###############################################################################
def create_intermediate_dir(dir_) :    
    if not os.path.isdir(dir_) :
        os.mkdir(dir_)
        
def create_dir(path):
    split_path = path.split(os.sep)
    current_path = ''
    for part in split_path:
        if part != '':
            current_path += part + '/'
            create_intermediate_dir(current_path)
###############################################################################   
