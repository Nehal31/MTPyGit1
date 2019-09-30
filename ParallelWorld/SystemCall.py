import sysconfig

platform = sysconfig.get_platform()
print(platform)
if platform == 'win32':
    print("Window System")

import sys
print(sys.version)


import os
print(os.getcwd())
print(os.chdir('..'))
print(os.getcwd())

