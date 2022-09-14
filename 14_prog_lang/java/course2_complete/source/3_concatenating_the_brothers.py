import os
from shutil import copyfile

WRKING_DIRECTORY = "3_just_java_good_names"

####
# 1) Creation of a file with titles
####

input_folder = WRKING_DIRECTORY
l_files_in = []
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        l_files_in.append(os.path.join(path, name))

l_to_write_titles = l_files_in.copy()
for i in range(len(l_to_write_titles)):
    l_to_write_titles[i] = l_to_write_titles[i].replace("3_just_java_good_names\\", "")
with open('4_outputs/titles.txt', 'w') as f:
    for item in l_to_write_titles:
        f.write("%s\n" % item)

####
# 2) Concatenation of all files
####

with open('4_outputs/concatenated.txt', 'w') as concatenated_file:
    concatenated_file.write("Codes Used on the Course\n")
    for item in l_to_write_titles:
        concatenated_file.write("%s\n" % item)
    concatenated_file.write("\f")

    for i in range(len(l_files_in)):
        with open(l_files_in[i]) as infile:
            concatenated_file.write("##--> " + l_to_write_titles[i] + "<-- ##")
            concatenated_file.write("\n\n")
            concatenated_file.write(infile.read())
            concatenated_file.write("\f")


