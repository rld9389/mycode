#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')

#move raynor to ceph_storage
shutil.move('raynor.obj', 'ceph_storage/')

#prompt the user for a new name for the kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')

#rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


