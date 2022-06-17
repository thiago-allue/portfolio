import glob
import os

folder_path = '.'
for filename in glob.glob(os.path.join(folder_path, '*.py')):
  with open(filename, 'r') as f:
    text = f.read()
    print ("\n\n### " + filename + " ####################################")
    print (text)