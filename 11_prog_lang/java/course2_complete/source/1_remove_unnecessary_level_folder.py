import os
from shutil import copyfile

# 1. get the list of all files inside "just_java_sample_input"
input_folder = "just_java_sample_input"
l_files_in = []
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        l_files_in.append(os.path.join(path, name))


# 2. create another list removing the undesired levels
l_files_out = l_files_in.copy()

for i in range(len(l_files_out)):
    l_files_out[i] = l_files_out[i].replace("\\src", "")
    l_files_out[i] = l_files_out[i].replace("\\com", "")
    l_files_out[i] = l_files_out[i].replace("\\udemy", "")
    l_files_out[i] = l_files_out[i].replace("\\app", "")
    l_files_out[i] = l_files_out[i].replace("input", "output")

# 3. For each file in l_input, copy to the destiny l_output
for i in range(len(l_files_in)):
    copyfile(l_files_in[i], l_files_out[i])
