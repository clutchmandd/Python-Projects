import shutil
import os

# set where the source of the files are
source = '/Users/dixon/Documents/GitHub/Python-Projects/File_Transfer_Assignment/Folder_A/'

#set the destination path to Folder_B
destination = '/Users/dixon/Documents/GitHub/Python-Projects/File_Transfer_Assignment/Folder_B/'
files = os.listdir(source)

for i in files:
    # moving the files represented by 'i' to their new destination
    shutil.move(source+i,destination)
