import os
from shutil import copyfile

# creation of a single and concatenated file with:
#   - title of the file
#   - break of page for each start of file

# 1. get the list of all files inside "2_just_java_removed_levels"
input_folder = "2_just_java_removed_levels"
l_files_in = []
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        l_files_in.append(os.path.join(path, name))

# 2. Copy them to the origin with the prefix of the folder
l_files_out = l_files_in.copy()

for i in range(len(l_files_out)):
    l_files_out[i] = l_files_out[i].replace("\\", "_")
    l_files_out[i] = l_files_out[i].replace("2_just_java_removed_levels_", "2_just_java_removed_levels\\")

assert True
for i in range(len(l_files_in)):
    copyfile(l_files_in[i], l_files_out[i])

# 3. Remove manually the folders

