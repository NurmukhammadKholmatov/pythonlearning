#-*- conding: utf-8 -*-
# Нужно собрать информацию об операционной системе и версии пайтона


import os
import platform
import sys


info = 'Os info is \n{}\n\nPython version is {} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)
with open('os_info.txt', 'w') as ff:
     ff.write(info)