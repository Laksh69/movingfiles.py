import os
import shutil
#store the path of downloads folder in variable from_Dir
from_dir="/Users/richakapoor/Downloads"
#create a folder with name document files in the system.
#store the path of document files folder in variable to_dir
to_dir="/Users/richakapoor/Desktop/schoolwork"


list_of_files=os.listdir(from_dir)
#print(list_of_files)

for fileName in list_of_files:
    name,extension=os.path.splitext(fileName)