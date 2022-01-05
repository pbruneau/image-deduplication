# move all files in a directory tree to the directory root
# unsafe if file names are not unique

import shutil
import os

folder = "Folder"

for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        if os.path.exists(os.path.join(folder, filename)):
            fname, extension = os.path.splitext(filename)
            i = 1
            while os.path.exists(fname + "_" + str(i) + extension):
                i += 1
            target_fname = fname + "_" + str(i) + extension
        else:
            target_fname = filename
        
        shutil.copy(os.path.join(root, filename), os.path.join(folder, target_fname))
