#!/usr/bin/env python3
import shutil
import os

#The following will change the home user directory 
os.chdir('/home/student/mycode/')

#The following line will create the copy of the file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network_copy.txt')

#The following line will create a backup of the directory
shutil.copytree('5g_research/', '5g_research_backup/')

