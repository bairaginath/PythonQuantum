__author__ = 'veradocs-web'


import os
print os.getcwd()      # Return the current working directory

os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir today') # Run the command mkdir in the system shell



dir(os)
help(os)

# For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use:
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')


# The glob module provides a function for making file lists from directory wildcard searches:
import glob
glob.glob('*.py')


import sys
print sys.argv

sys.stderr.write('Warning, log file not found starting a new one\n')





